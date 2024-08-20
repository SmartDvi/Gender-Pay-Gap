# Gender Pay Gap Dashboard

![Dashboard Image](https://github.com/SmartDvi/Gender-Pay-Gap/blob/main/Animation.gif)  

## Overview

This project provides an interactive dashboard to analyze the Gender Pay Gap data in Ireland. The dashboard visualizes key metrics, such as mean and median hourly pay gaps, bonus distributions, and the financial impact of closing the gender pay gap. The data is sourced from publicly available reports as required by the Irish Gender Pay Gap Information Act.

The project aims to promote transparency and facilitate data-driven discussions around gender equality in the workplace. The dashboard is built using Python with Dash, Plotly, Dash Bootstrap Components, and Dash Mantine Components.

## Features

- **Industry and Company Selection:** Allows users to filter data by industry and select specific companies for detailed analysis.
- **Key Metrics Visualization:** Displays total payroll costs, bonuses, and the impact of closing the gender pay gap.
- **Data Insights:** Offers insights into the gender distribution of employees, bonus distribution, and potential savings if the pay gap is reduced.
- **Interactive Tabs:** Enables users to navigate between different data views, including detailed datasets, gender representation, and bonus distribution.

## Dataset

The dataset used in this project is compiled from publicly available reports on the Irish gender pay gap. The data includes information on mean and median hourly pay gaps, bonus distributions, employee gender distribution, and other relevant metrics. The dataset is updated regularly to reflect new reports.

### Dataset Columns

- `id`: A unique ID for each record.
- `companyName`: The name of the company.
- `companies_ID`: An ID linking to the records in the companies table.
- `meanBonus`: The percentage difference in mean bonus remuneration between male and female employees.
- `meanHourly`: The percentage difference in mean hourly remuneration between male and female employees.
- `medianBonus`: The percentage difference in median bonus remuneration between male and female employees.
- `medianHourly`: The percentage difference in median hourly remuneration between male and female employees.
- `reportLink`: A link to the relevant report.
- `year`: The year of the relevant report.
- `meanHourlyPT`: The percentage difference in mean hourly remuneration for part-time employees between male and female employees.
- `medianHourlyPT`: The percentage difference in median hourly remuneration for part-time employees between male and female employees.
- `meanHourlyTemp`: The percentage difference in mean hourly remuneration for temporary employees between male and female employees.
- `medianHourlyTemp`: The percentage difference in median hourly remuneration for temporary employees between male and female employees.
- `perBonusFemale`: The percentage of female employees who were paid a bonus.
- `perBonusMale`: The percentage of male employees who were paid a bonus.
- `perBIKFemale`: The percentage of female employees who received benefits in kind.
- `perBIKMale`: The percentage of male employees who received benefits in kind.
- `pb1Female`: The percentage of female employees in the lower remuneration quartile.
- `pb1Male`: The percentage of male employees in the lower remuneration quartile.
- `pb2Female`: The percentage of female employees in the lower middle remuneration quartile.
- `pb2Male`: The percentage of male employees in the lower middle remuneration quartile.
- `pb3Female`: The percentage of female employees in the upper middle remuneration quartile.
- `pb3Male`: The percentage of male employees in the upper middle remuneration quartile.
- `pb4Female`: The percentage of female employees in the upper remuneration quartile.
- `pb4Male`: The percentage of male employees in the upper remuneration quartile.
- `perEmployeesFemale`: The percentage of overall employees who are female.
- `perEmployeesMale`: The percentage of overall employees who are male.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/SmartDvi/Gender-Pay-Gap.git
cd Gender-Pay-Gap
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Running the Dashboard

```bash
python app.py
```

Once the server is running, open your browser and go to `http://127.0.0.1:8050/` to view the dashboard.

## Usage

### Navigating the Dashboard

- **Industry Selection:** Use the dropdown menu to filter data by industry.
- **Company Selection:** After selecting an industry, choose a company to view specific metrics.
- **Tabs:** Use the tabs to switch between different views, including dataset details, gender representation, and bonus distribution analysis.

### Data Updates

The dataset is regularly updated. To add new data, follow these steps:

1. **Check if the company exists:** Look for the company in `companies.csv`.
2. **Add new data:** If the company exists, add the new data to `gpg.csv` and ensure the "id" field is unique.
3. **New company record:** If the company doesn't exist, add the company to `companies.csv` before adding data to `gpg.csv`.

You can also contribute data via the web form available at [paygap.ie/newReport](https://paygap.ie/newReport).

## License

This project is licensed under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. For more details, refer to the [LICENSE](LICENSE) file.

## Acknowledgments

- Thanks to the contributors who help keep the dataset up to date.
- Special shoutout to the open-source community for providing tools and libraries that make projects like this possible.

## Contributions

Contributions to the project are welcome. If you would like to contribute, please fork the repository, make your changes, and submit a pull request.
