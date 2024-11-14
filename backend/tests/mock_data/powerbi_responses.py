from typing import Dict, Any

class PowerBIMockData:
    @staticmethod
    def get_dataset_response() -> Dict[str, Any]:
        return {
            "value": [
                {
                    "id": "dataset-123",
                    "name": "Sales Analysis",
                    "configuredBy": "user@domain.com",
                    "defaultRetentionPolicy": "None",
                    "tables": [
                        {
                            "name": "Sales",
                            "columns": [
                                {"name": "OrderDate", "dataType": "dateTime"},
                                {"name": "Revenue", "dataType": "decimal"},
                                {"name": "Quantity", "dataType": "int64"},
                                {"name": "ProductKey", "dataType": "int64"}
                            ]
                        },
                        {
                            "name": "Products",
                            "columns": [
                                {"name": "ProductKey", "dataType": "int64"},
                                {"name": "ProductName", "dataType": "string"},
                                {"name": "Category", "dataType": "string"},
                                {"name": "UnitPrice", "dataType": "decimal"}
                            ]
                        },
                        {
                            "name": "DateTable",
                            "columns": [
                                {"name": "Date", "dataType": "dateTime"},
                                {"name": "Year", "dataType": "int64"},
                                {"name": "Month", "dataType": "string"},
                                {"name": "Quarter", "dataType": "string"}
                            ]
                        }
                    ],
                    "relationships": [
                        {
                            "name": "Sales_Products",
                            "fromTable": "Sales",
                            "fromColumn": "ProductKey",
                            "toTable": "Products",
                            "toColumn": "ProductKey",
                            "crossFilteringBehavior": "bothDirections"
                        },
                        {
                            "name": "Sales_Dates",
                            "fromTable": "Sales",
                            "fromColumn": "OrderDate",
                            "toTable": "DateTable",
                            "toColumn": "Date",
                            "crossFilteringBehavior": "bothDirections"
                        }
                    ],
                    "measures": [
                        {
                            "name": "Total Revenue",
                            "expression": "SUM(Sales[Revenue])",
                            "formatString": "$#,##0.00"
                        },
                        {
                            "name": "YTD Revenue",
                            "expression": "TOTALYTD(SUM(Sales[Revenue]), DateTable[Date])",
                            "formatString": "$#,##0.00"
                        }
                    ]
                }
            ]
        }

    @staticmethod
    def get_report_response() -> Dict[str, Any]:
        return {
            "value": [
                {
                    "id": "report-456",
                    "name": "Sales Dashboard",
                    "embedUrl": "https://app.powerbi.com/reportEmbed",
                    "webUrl": "https://app.powerbi.com/reports/report-456",
                    "pages": [
                        {
                            "name": "Overview",
                            "displayName": "Sales Overview",
                            "visuals": [
                                {
                                    "name": "Revenue by Category",
                                    "type": "columnChart",
                                    "title": "Revenue by Product Category"
                                },
                                {
                                    "name": "Monthly Trend",
                                    "type": "lineChart",
                                    "title": "Monthly Revenue Trend"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    @staticmethod
    def get_dax_query_response() -> Dict[str, Any]:
        return {
            "results": [
                {
                    "tables": [
                        {
                            "rows": [
                                {
                                    "Total Revenue": 1250000.00,
                                    "YTD Revenue": 750000.00
                                }
                            ]
                        }
                    ]
                }
            ]
        } 