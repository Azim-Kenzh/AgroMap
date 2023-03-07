from threading import Thread

import matplotlib.pyplot as plt
from rest_framework.response import Response
from rest_framework.views import APIView

from gip.models import ContourYear
from indexes.models import ContourAverageIndex, ProductivityClass
from drf_yasg.utils import swagger_auto_schema


class CreatingAverage(APIView):
    @swagger_auto_schema(
        operation_summary='for now do not required for front'
    )
    def post(self, request, *args, **kwargs):
        """
        required query_params:
        - date
        - start
        - end
        """

        start = self.request.query_params['start']
        end = self.request.query_params['end']

        for i in range(int(start), int(end)):
            try:
                contour = ContourYear.objects.get(id=i)
                pruductivity = ProductivityClass.objects.get(id=1)
                ContourAverageIndex.objects.create(contour=contour, productivity_class=pruductivity)
            except Exception as e:
                with open(f'reportCreatingAverage.txt', 'a') as file:
                    file.write(f"{i}' = f'{e}")
                    file.write(',')
                    file.write('\n')
                    plt.close()
                pass

        return Response('started')
