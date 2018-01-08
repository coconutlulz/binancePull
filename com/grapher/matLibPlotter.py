import matplotlib.pyplot as plot, mpld3

class matLibPlotter():
        
    def pie_plotter(self, values, labels, title):
        plot.pie(values, labels=labels, startangle=90, shadow=True, explode=(0,0,0.1,0,0,0), autopct='%.2f%%' )
        plot.title(title)
        plot.legend()
        print(mpld3.fig_to_html(plot.figure()))
        mpld3.show()


labels = ['XLM', 'XRP', 'REQ', 'APPC', 'BRD', 'VEN']
values = [0.10115000, 0.11366832, 0.29299256, 0.02868976, 0.03473600, 0.06777753]
values = [v*10 for v in values]
    

matLibPlotter().pie_plotter(values, labels, "Crypto")