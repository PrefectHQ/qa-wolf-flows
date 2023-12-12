from prefect import flow, task
from prefect.artifacts import create_markdown_artifact, create_link_artifact, create_table_artifact

@task
def my_first_link_task():
        create_link_artifact(
            key="variable-data-link",
            link="https://nyc3.digitaloceanspaces.com/my-bucket-name/highly_variable_data_.csv",
            description="## Highly variable data",
            link_text="Highly variable data",
        )

@task
def my_second_link_task():
        create_link_artifact(
            key="variable-data-link",
            link="https://nyc3.digitaloceanspaces.com/my-bucket-name/low_pred_data_.csv",
            description="# Low prediction accuracy data",
        )
@task
def my_table_task():
    highest_churn_possibility = [
       {'customer_id':'12345', 'name': 'John Smith', 'churn_probability': 0.85 }, 
       {'customer_id':'56789', 'name': 'Jane Jones', 'churn_probability': 0.65 } 
    ]

    create_table_artifact(
        key="personalized-reachout",
        table=highest_churn_possibility,
        description= "# Marvin, please reach out to these customers today!"
    )
    
@task
def markdown_task():
    na_revenue = 500000
    markdown_report = f"""# Sales Report

## Summary

In the past quarter, our company saw a significant increase in sales, with a total revenue of $1,000,000. This represents a 20% increase over the same period last year.

## Sales by Region

| Region        | Revenue |
|:--------------|-------:|
| North America | ${na_revenue:,} |
| Europe        | $250,000 |
| Asia          | $150,000 |
| South America | $75,000 |
| Africa        | $25,000 |

## Top Products

1. Product A - $300,000 in revenue
2. Product B - $200,000 in revenue
3. Product C - $150,000 in revenue

## Conclusion

Overall, these results are very encouraging and demonstrate the success of our sales team in increasing revenue across all regions. However, we still have room for improvement and should focus on further increasing sales in the coming quarter.
"""
    create_markdown_artifact(
        key="gtm-markdown-report",
        markdown=markdown_report,
        description="Quarterly Sales Report",
    )

@flow()
def artifacts_flow():
    '''Flow that creates markdown, link and table artifacts
    
## Flow code
```python
from prefect import flow, task
from prefect.artifacts import create_markdown_artifact, create_link_artifact, create_table_artifact

@task
def my_first_link_task():
        create_link_artifact(
            key="variable-data-link",
            link="https://nyc3.digitaloceanspaces.com/my-bucket-name/highly_variable_data_.csv",
            description="## Highly variable data",
            link_text="Highly variable data",
        )

@task
def my_second_link_task():
        create_link_artifact(
            key="variable-data-link",
            link="https://nyc3.digitaloceanspaces.com/my-bucket-name/low_pred_data_.csv",
            description="# Low prediction accuracy data",
        )
@task
def my_table_task():
    highest_churn_possibility = [
       {'customer_id':'12345', 'name': 'John Smith', 'churn_probability': 0.85 }, 
       {'customer_id':'56789', 'name': 'Jane Jones', 'churn_probability': 0.65 } 
    ]

    create_table_artifact(
        key="personalized-reachout",
        table=highest_churn_possibility,
        description= "# Marvin, please reach out to these customers today!"
    )
    
@task
def markdown_task():
    na_revenue = 500000
    markdown_report = f"""# Sales Report

## Summary

In the past quarter, our company saw a significant increase in sales, with a total revenue of $1,000,000. This represents a 20% increase over the same period last year.

## Sales by Region

| Region        | Revenue |
|:--------------|-------:|
| North America | ${na_revenue:,} |
| Europe        | $250,000 |
| Asia          | $150,000 |
| South America | $75,000 |
| Africa        | $25,000 |

## Top Products

1. Product A - $300,000 in revenue
2. Product B - $200,000 in revenue
3. Product C - $150,000 in revenue

## Conclusion

Overall, these results are very encouraging and demonstrate the success of our sales team in increasing revenue across all regions. However, we still have room for improvement and should focus on further increasing sales in the coming quarter.
"""
    create_markdown_artifact(
        key="gtm-markdown-report",
        markdown=markdown_report,
        description="Quarterly Sales Report",
    )

@flow()
def artifacts_flow():
    markdown_task()
    my_first_link_task()
    my_second_link_task()
    my_table_task()
    
```
    '''
    markdown_task()
    my_first_link_task()
    my_second_link_task()
    my_table_task()
    

