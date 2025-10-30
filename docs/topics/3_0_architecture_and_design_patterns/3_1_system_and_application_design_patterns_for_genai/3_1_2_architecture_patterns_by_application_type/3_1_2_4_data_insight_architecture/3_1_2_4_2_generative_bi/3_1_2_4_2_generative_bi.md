<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Generative BI: Natural Language-Based Data Visualization

**Content Level:** 300

## Suggested Pre-Reading
- [Text-to-SQL Application](../3_1_2_4_1_text_to_sql_application/3_1_2_4_1_text_to_sql_application.md)
- [Data Insight Architecture](../index.md)
- [Foundation Architecture Components](../../../3_1_1_foundation_architecture_components/index.md)

## TL;DR

Generative BI extends Text-to-SQL by automating the entire analytics workflow from natural language questions to interactive visualizations. Unlike traditional BI's pre-built dashboards, Generative BI dynamically creates charts and insights based on user requests. Success depends on building a robust semantic layer that maps business terminology to data structures and choosing the right approach between data conversion for simple cases and code generation for complex analysis.

## Generative BI Overview

Generative BI extends Text-to-SQL by automating the complete journey from natural language questions to interactive visualizations. While Text-to-SQL generates queries, Generative BI also selects appropriate chart types, applies business context, and creates ready-to-use dashboards.

Traditional BI systems and Generative BI differ fundamentally in their architecture and approach:

**Traditional BI Systems** rely on pre-defined dashboards and reports developed using GUI-based tools. They are typically managed and maintained by technical experts, with long development cycles for change requests.

**Generative BI Systems** enable instant visualization through natural language interfaces, based on code-first declarative definitions (BI-as-Code). They automate visualization creation and data querying through AI models and support iterative improvement through user feedback.

## Architecture Components

Generative BI systems operate through three coordinated layers that transform natural language requests into interactive visualizations:

**Visualization Layer** handles user interaction and chart rendering. When a user asks "Show revenue trends by region," this layer interprets the intent and determines the appropriate chart type (likely a line chart with regional grouping).

**Data Transformation Layer** bridges natural language and data through Text-to-SQL conversion and semantic mapping. It translates "revenue trends" to `SUM(sales_amount)` grouped by time periods and regions.

**Data Layer** provides secure, optimized access to underlying databases with appropriate access controls and performance optimization for visualization workloads.

In enterprise environments, a **data catalog** complements these layers by serving as the comprehensive inventory system for all data assets. While the semantic layer helps AI understand what data means, the data catalog helps it understand what data exists and where to find it. The catalog maintains metadata about data sources, business context, and usage patterns, enabling the AI to locate relevant datasets and understand their governance requirements. Together with the semantic layer, this creates a knowledge framework that allows generative AI to generate accurate, contextual insights while maintaining proper data governance.

## What is Semantic Layer?

The semantic layer is particularly important for Generative BI because it provides the business context necessary to interpret natural language queries accurately. Unlike traditional BI where metrics are pre-calculated and reports pre-defined, Generative BI must dynamically interpret what users are asking and construct appropriate calculations on demand.

```yaml
# Semantic layer definition example
metric:
  name: "Revenue Growth Rate"
  business_definition: "Month-over-month percentage increase in total revenue"
  technical_definition: "((current_month_revenue / previous_month_revenue) - 1) * 100"
  related_terms: ["MoM Growth", "Revenue Increase"]
  recommended_visualization: "line_chart"
  business_context: "Key indicator for quarterly performance reviews"
  calculation_components:
    current_month_revenue: "SUM(sales.amount) WHERE date_trunc('month', sales.date) = :current_month"
    previous_month_revenue: "SUM(sales.amount) WHERE date_trunc('month', sales.date) = :previous_month"
```

This semantic definition enables accurate interpretation of questions about "growth rate" or "revenue trends," generation of complex calculations not explicitly stored in the database, consistent calculation methodology across all visualizations, and business-context aware visualization selection.

### Example in Practice:

When a business user asks a generative BI system: "Show me last quarter's sales performance by region compared to targets"

The semantic layer translates this to:
- What "sales performance" means (which tables, fields, calculations)
- What defines "last quarter" (date logic)
- What "region" refers to (geographic hierarchy)
- Where "targets" data comes from and how it relates to sales data

Without a semantic layer, the generative AI would have to somehow figure out complex database structures, join relationships, and business logic on its own, which would be extremely difficult and error-prone. The semantic layer effectively "teaches" the AI about your business context, enabling it to generate meaningful insights rather than just manipulating raw data.

### Building the Semantic Layer

Developing an effective semantic layer requires a methodical approach. Begin by identifying core business concepts, defining key metrics and KPIs while collecting frequently used business terms and abbreviations. Next, map these concepts to your data model by linking business terms to actual database tables and columns and defining necessary join relationships.

Standardization is key—establish consistent methods for metric calculations and specify appropriate aggregation levels and filter conditions for different business scenarios. For visualization clarity, define recommended chart types for each metric category and establish consistent color schemes and threshold values that align with your organization's reporting standards.

Finally, create a process for continuous improvement where semantic definitions are refined based on user feedback and new business concepts can be systematically incorporated as your organization's needs evolve. In AWS QuickSight, the Q Topics feature serves a similar purpose, providing business context through field definitions, synonyms, and semantic types that enable accurate natural language query interpretation.

## Implementation Approaches

Generative BI systems can create visualizations through two primary methods:

### Data Conversion Approach
Structures query results according to predefined chart templates:
```json
// Transformed data structure example
{
  "chart_type": "bar_chart",
  "data": {
    "labels": ["North", "South", "East", "West"],
    "datasets": [{
      "label": "2023 Revenue",
      "data": [1250000, 980000, 870000, 1120000]
    }]
  },
  "options": {
    "title": "Revenue by Region",
    "xAxis_title": "Region",
    "yAxis_title": "Revenue ($)"
  }
}
```

**Pros**: Consistent outputs, easier validation, lower error rates
**Cons**: Limited to predefined templates, not suitable for large datasets

### Code Generation Approach
Uses LLMs to generate custom visualization code:

```python
# Generated visualization code example
def create_sales_by_region_chart(data):
    # Sample large datasets
    if len(data) > 10000:
        data = stratified_sampling(data, 10000)
    
    # Aggregate data
    region_sales = data.groupby('region')['sales_amount'].sum().reset_index()
    region_sales = region_sales.sort_values('sales_amount', ascending=False)
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x='region', y='sales_amount', data=region_sales)
    plt.title('Revenue by Region')
    plt.ylabel('Revenue ($)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
```

**Pros**: Handles large datasets, supports custom requirements, data-specific optimizations
**Cons**: Higher error potential, requires code execution environment

**When to Choose**: Use data conversion for standard business reports with consistent formats. Use code generation for exploratory analysis requiring custom visualizations or handling large datasets.


## Making it Practical

**Start with Core Business Metrics**: Begin with 10-15 frequently asked business questions in one domain. Build semantic definitions for these first, then expand based on actual usage patterns rather than trying to cover everything upfront.

**Build Semantic Layer Incrementally**: Define business terminology mappings, calculation methods, and visualization preferences for your most important KPIs. Example: Map "revenue growth" to specific SQL calculations and recommend line charts for trend visualization.

**Choose Implementation Strategy**: Use data conversion templates for standard reports (faster, more reliable) and code generation for custom analysis (flexible but requires validation). Monitor which approach works better for different question types.

**Establish Feedback Loops**: Track visualization accuracy, user corrections, and common failure patterns. Use this data to improve semantic definitions and expand your template library based on proven successful patterns.


## Further Reading

- <a href="https://aws.amazon.com/blogs/business-intelligence/enhance-your-analytics-embedding-experience-with-generative-bi-capabilities/" target="_blank" rel="noopener noreferrer">Enhance Your Analytics Embedding Experience with Generative BI Capabilities - AWS Blog</a>

## Contributors

**Author**:

* Kihyeon Myung - Senior Applied AI Architect 

**Primary Reviewer**:

* Manoj Ramani - Senior Applied AI Architect 
* Don Simpson - Principal Technologist 
