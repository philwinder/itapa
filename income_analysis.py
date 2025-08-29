import folium
import geopandas as gpd
import pandas as pd

# Read the income data
df = pd.read_excel('income_estimates_2020.xlsx', 
                   sheet_name='Total annual income',
                   header=4)

# Read the MSOA boundaries
msoa_boundaries = gpd.read_file('MSOA_Dec_2011_Boundaries_Super_Generalised_Clipped_BSC_EW_V3_2022_-5254045062471510471.geojson')

# Ensure MSOA codes match between datasets
msoa_boundaries['MSOA11CD'] = msoa_boundaries['MSOA11CD'].astype(str)
df['MSOA code'] = df['MSOA code'].astype(str)

# Merge the datasets
merged_data = msoa_boundaries.merge(df, 
                                  left_on='MSOA11CD', 
                                  right_on='MSOA code')

# Create a base map centered on the UK
m = folium.Map(location=[53, -2], zoom_start=6)

# Create custom bins for more contrast
income_values = df['Total annual income (£)']
bins = list(income_values.quantile([0, 0.2, 0.4, 0.6, 0.8, 1]))

# Add the choropleth layer with custom colors
folium.Choropleth(
    geo_data=merged_data.__geo_interface__,
    name='choropleth',
    data=df,
    columns=['MSOA code', 'Total annual income (£)'],
    key_on='feature.properties.MSOA11CD',
    fill_color='RdYlBu_r',  # Changed to reversed Red-Yellow-Blue for more contrast
    fill_opacity=0.8,  # Increased opacity
    line_opacity=0.2,
    legend_name='Total Annual Income (£)',
    bins=bins,
    highlight=True
).add_to(m)

# Add tooltips for better interactivity
style_function = lambda x: {'fillColor': '#ffffff', 
                          'color':'#000000', 
                          'fillOpacity': 0.1, 
                          'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                              'color':'#000000', 
                              'fillOpacity': 0.50, 
                              'weight': 0.1}

tooltip = folium.features.GeoJson(
    merged_data,
    style_function=style_function,
    control=False,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['MSOA name', 'Total annual income (£)'],
        aliases=['Area:', 'Annual Income:'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
    )
)
m.add_child(tooltip)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map
m.save('income_heatmap.html')