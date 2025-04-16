import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'projectcampur-cb81d0b972c2.json'
export = "[PATH]"

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
    GetMetadataRequest
)


def sample_run_report(property_id="485511477"):
    """Runs a simple report on a Google Analytics 4 property."""
    # TODO(developer): Uncomment this variable and replace with your
    #  Google Analytics 4 property ID before running the sample.
    # property_id = "YOUR-GA4-PROPERTY-ID"

    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2025-03-31", end_date="today")],
    )
    response = client.run_report(request)

    print("Report result:")
    for row in response.rows:
        print(row.dimension_values[0].value, row.metric_values[0].value)


sample_run_report()

# property_id="485511477"
# client = BetaAnalyticsDataClient()
# request = GetMetadataRequest(name=f"properties/{property_id}/metadata")
# response = client.get_metadata(request)
# print("📏 Available Metrics:")
# for metric in response.metrics:
#     print(f"- {metric.api_name}: {metric.ui_name}")

# print("\n📐 Available Dimensions:")
# for dimension in response.dimensions:
#     print(f"- {dimension.api_name}: {dimension.ui_name}")

#########

# property_id = "485511477"

# client = BetaAnalyticsDataClient()

# request = GetMetadataRequest(name=f"properties/{property_id}/metadata")
# response = client.get_metadata(request)

# print("📐 Realtime Dimensions:")
# for dim in response.dimensions:
#     if dim.realtime:
#         print(f"- {dim.api_name} ({dim.ui_name})")

# print("\n📏 Realtime Metrics:")
# for met in response.metrics:
#     if met.realtime:
#         print(f"- {met.api_name} ({met.ui_name})")