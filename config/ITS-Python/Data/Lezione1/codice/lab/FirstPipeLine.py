import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataPipeLine():
    def __init__(self)-> None:
        self.csv_path: str = "../dati/raw_data.csv"
        self.clean_csv_path: str = "../dati/clean_data.csv"
        self.output_plot = "../visual/scatter_plot.png"
    def caricamento_dati(self)-> pd.DataFrame:
        # Lettura dal csv
        df: pd.DataFrame = pd.read_csv(self.csv_path)
        return df

    def salvataggio_dati(self, df: pd.DataFrame)-> None:
        df.to_csv(self.clean_csv_path, index = False)

    def processamento_dati(self, df: pd.DataFrame)-> pd.DataFrame:
        df["is_healthy"] = (df["screen_time_hours"] < 4) & (df["sleep_hours"] >= 8)
        # self.slavataggio_dati(df)
        return df

    def visualizzazione_dati(self, df: pd.DataFrame)-> None:
        # Visualizzazione datis
        '''
        plt.figure(figsize=(10,6))
        true_data: pd.DataFrame = df[df["is_healty"] == True]
        false_data: pd.DataFrame = df[df["is_healty"] == False]
        plt.scatter(true_data["screen_time_hours"], true_data["math_score"], color="green", label = "True")
        plt.scatter(false_data["screen_time_hours"], false_data["math_score"], color="red", label = "False")
        plt.xlabel("Screen time hours")
        plt.ylabel("Math score")
        plt.title("Screen time hours vs math score")
        plt.legend()
        plt.savefig(self.output_plot)
        plt.close()
        '''
        plt.figure(figsize=(10,6))
        plt.title("Screen time hours vs math score")
        sns.scatterplot(data=df, x="screen_time_hours", y="math_score", hue="is_healthy")
        plt.savefig(self.output_plot)
        plt.close()


    def esegui_pipeline(self)-> None:
        # Caricamneto
        raw_df: pd.DataFrame = self.caricamento_dati()
        print("    -Letti dati da un csv")
        # print(raw_df)
        # Preprocessamento
        clean_df = self.processamento_dati(raw_df)
        print("    -Pulizia dati completata e file salvato")
        #print(clean_df.columns)
        self.visualizzazione_dati(clean_df)
        print("    -Visualizzati e salvati dati di analisi")

if __name__ == "__main__":
    pipe_line:DataPipeLine = DataPipeLine()
    print("Pipeline avviata...")
    pipe_line.esegui_pipeline()
    print("...Pipeline completata")