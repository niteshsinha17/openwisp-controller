from django.urls import path


def get_geo_urls(geo_views):
    return [
        path(
            'api/v1/device/<str:pk>/location/',
            geo_views.device_location,
            name='device_location',
        ),
        path('api/v1/location/geojson/', geo_views.geojson, name='location_geojson',),
        path(
            'api/v1/location/<str:pk>/device/',
            geo_views.location_device_list,
            name='location_device_list',
        ),
    ]
