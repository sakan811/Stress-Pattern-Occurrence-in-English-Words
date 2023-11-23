import altair as alt
import pandas as pd


def load_data(data_path):
    # Added a return statement to return the loaded data
    return pd.read_csv(data_path, delimiter='\t')


def save_chart(chart, output_path):
    # Save the chart as an SVG file
    alt.Chart.save(chart, output_path)


def create_base_bar_chart(grouped_data, title, height, width):
    # Base chart
    base_chart = alt.Chart(grouped_data).encode(
        x=alt.X('stress_pattern:O', title='Stress Pattern', axis=alt.Axis(labelAngle=0))
    ).properties(
        title=title,
        height=height,
        width=width  # Adjust width to make the chart wider
    )

    return base_chart


def create_bar_chart_quantity(grouped_data, title, height, width, output_path):

    base_chart = create_base_bar_chart(grouped_data, title, height, width)

    # Bar layer
    bars = base_chart.mark_bar(size=50).encode(
        y=alt.Y('count:Q', title='Count')
    )

    # Text layer
    text = base_chart.mark_text(align='center', baseline='bottom', dy=-2, fontSize=20).encode(
        y=alt.Y('count:Q', title='Count'),
        text='count:Q'
    )

    # Combined chart with configuration
    chart = (bars + text).configure_axis(
        labelFontSize=20,
        titleFontSize=20
    ).configure_title(
        fontSize=25
    )

    save_chart(chart, output_path)


def count_pattern(data_path, column_name, length):
    # Load the data from the TSV file
    dataframe = load_data(data_path)

    # Pad values in a specified column with zeros.
    dataframe = pad_with_zeros(dataframe, column_name, length)

    # Group by stress_pattern and count the occurrences
    grouped_data = dataframe.groupby('stress_pattern').size().reset_index(name='count')

    return grouped_data


def filter_data(grouped_data, data_num):
    # Sort the grouped_data by 'count' in descending order and keep only the specific number of data
    top_5_groups = grouped_data.sort_values(by='count', ascending=False).head(data_num)

    return top_5_groups


def pad_with_zeros(dataframe, column_name, length):
    # Convert the column values to strings
    dataframe[column_name] = dataframe[column_name].astype(str)

    # Pad the string values with zeros
    dataframe[column_name] = dataframe[column_name].apply(lambda x: x.zfill(length))

    return dataframe


def main():
    for i in range(2, 7):
        data = f'../dataset/Syllables with Stress Pattern/{i}_with_stress_patterns.tsv'

        column_name = 'stress_pattern'

        length = i  # set to the number of syllable to pad zeros correctly.
        data = count_pattern(data, column_name, length)

        # Specified number of data in the chart
        data_filtered = filter_data(data, data_num=5)

        title = f'Stress Pattern in {length}-Syllable English Words'

        height = 1800
        width = 3200

        output_path_q = f'../graph_svg/{length}-syllable_graph_quantity.svg'
        output_path_t5 = f'../graph_svg/{length}-syllable_graph_top_5.svg'

        create_bar_chart_quantity(data, title, height, width, output_path_q)

        # To create a chart with only number of data specified
        create_bar_chart_quantity(data_filtered, title, height, width, output_path_t5)


if __name__ == '__main__':
    main()

