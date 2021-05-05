import pandas as pd

from Base.FigureController import Controller


class ExpectationFromGovernmentFigureController(Controller):
    extension = 'eps'
    directory_name = "Expectation_From_Universities.eps"

    def process_data(self, **kwargs):
        # unique_values = self.get_unique_categories()
        plot_data = dict()

        for item in self.get_categories():
            if item in plot_data:
                plot_data[item] += 1
            else:
                plot_data[item] = 1

        self.plot_data = plot_data


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/universities.csv")
    controller = ExpectationFromGovernmentFigureController(df)
    controller.process_data()
    controller.draw_figure_bar_horizontally(save=True)
