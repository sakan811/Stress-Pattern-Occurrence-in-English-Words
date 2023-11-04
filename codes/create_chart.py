import altair as alt
import pandas as pd
import webbrowser
from altair_saver import save


def load_data(data_path):
    # Added a return statement to return the loaded data
    return pd.read_csv(data_path, delimiter='\t')


def save_chart(chart):
    # Save the chart as an HTML file
    save(chart, 'chart.html')

    # Open the HTML file in the default web browser
    webbrowser.open('chart.html')


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


def create_bar_chart_quantity(grouped_data, title, height, width):

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

    save_chart(chart)


def create_bar_chart_percent(grouped_data, title, height, width):

    base_chart = create_base_bar_chart(grouped_data, title, height, width)

    # To display the count as percentage
    total = grouped_data['count'].sum()
    grouped_data['percentage'] = ((grouped_data['count'] / total) * 100).round(2)

    # Bar layer
    bars = base_chart.mark_bar(size=50).encode(
        y=alt.Y('percentage:Q', title='Percentage')
    )

    # Text layer
    text = base_chart.mark_text(align='center', baseline='bottom', dy=-2, fontSize=20).encode(
        y=alt.Y('percentage:Q', title='Percentage'),
        text='percentage:Q'
    )

    # Combined chart with configuration
    chart = (bars + text).configure_axis(
        labelFontSize=20,
        titleFontSize=20
    ).configure_title(
        fontSize=25
    )

    save_chart(chart)


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


def group_pattern_percent(data_path, replacement_dict, column_name, length):
    # Load the data from the TSV file
    dataframe = load_data(data_path)

    # Pad values in a specified column with zeros.
    dataframe = pad_with_zeros(dataframe, column_name, length)

    # Define a function to group stress patterns
    def group_stress_pattern(pattern):
        if '1' in pattern:
            return ''.join(['1' if c == '1' else '0' for c in pattern])
        else:
            return pattern

    # Now apply the replacement
    dataframe['stress_pattern'] = dataframe['stress_pattern'].apply(group_stress_pattern)

    # Group by the updated 'stress_pattern' column and count the occurrences
    grouped_data = dataframe.groupby('stress_pattern').size().reset_index(name='count')

    return grouped_data


def pad_with_zeros(dataframe, column_name, length):
    # Convert the column values to strings
    dataframe[column_name] = dataframe[column_name].astype(str)

    # Pad the string values with zeros
    dataframe[column_name] = dataframe[column_name].apply(lambda x: x.zfill(length))

    return dataframe


def main():
    data = '6_with_stress_patterns.tsv'

    column_name = 'stress_pattern'
    length = 6  # set to the number of syllable to pad zeros correctly.
    data = count_pattern(data, column_name, length)

    # Uncomment this code in case to create a chart with only specific number of data.
    # data = filter_data(data, data_num=5)

    title = 'Stress Pattern in 6-Syllable English Words'

    height = 450
    width = 800

    create_bar_chart_quantity(data, title, height, width)

    # create_bar_chart_percent(data, title, height, width)


if __name__ == '__main__':
    main()
