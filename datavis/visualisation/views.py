from django.shortcuts import redirect, render
from src.processing.data_management import LoadPipeline
from src.processing.data_management import LoadIrisDataset
from config import config
from .chart import PlotPairplot, Plot3D
import pandas as pd

# Create your views here.

def index(request):
    return render(request, 'index.html')

def datavis(request):
    df = LoadIrisDataset()
    chart = PlotPairplot(df,config.ClfIrisSpecies_TARGET)
    plot = Plot3D(df, config.ClfIrisSpecies_TARGET)
    return render(request, 'datavis.html', { 'chart': chart,'plot': plot })

def size(request):
    df = LoadIrisDataset()
    pipeline_ClfIrisSpecies = LoadPipeline(
                                    model_name="ClfModel",
                                    path="outputs/trained_models")
    if request.method == 'POST':
        sepal_length = request.POST['slength']
        sepal_width = request.POST['swidth']
        petal_length = request.POST['plength']
        petal_width = request.POST['pwidth']
        X_live = pd.DataFrame(
            data={
                df.columns[0]: sepal_length,
                df.columns[1]: sepal_width,
                df.columns[2]: petal_length,
                df.columns[3]: petal_width
                },
            index=[0]
        )
        y_live = int(pipeline_ClfIrisSpecies.predict(X_live))
        y_liveProba = pipeline_ClfIrisSpecies.predict_proba(X_live)
        ProbText = ""
        for x in range(0,len(y_liveProba[0])):
            aux = f"	{config.ClfIrisSpecies_MAP[x]}: {round(y_liveProba[0][x],2)} \n "
            ProbText = ProbText + aux
            info= (
                f" The predicted class is {config.ClfIrisSpecies_MAP[y_live]} \n"
                f" The probability for each class is: \n\n "
                f"{ProbText}")
            return render(request, 'index.html',{'info': info})
    return redirect('index')