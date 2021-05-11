import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from Base.FigureController import Controller
from FigureGenerators.expectation_from_government import ExpectationFromGovernmentFigureController
from FigureGenerators.expectation_from_managers import ExpectationFromManagersFigureController
from FigureGenerators.expectation_from_new_hires import ExpectationFromNewHiresFigureController
from FigureGenerators.expectation_from_organization import ExpectationFromOrganizationFigureController
from FigureGenerators.expectation_from_peers import ExpectationFromPeersFigureController
from FigureGenerators.expectations_from_peers_employees import ExpectationFromPeersEmployeesFigureController


def show_bar_plot(df, class_name):
    controller_male = class_name(df[df['What is your Gender?'] == 'Male'])
    controller_female = class_name(df[df['What is your Gender?'] == 'Female'])
    controller_female.process_data()
    controller_male.process_data()
    all_keys = sorted(set().union(controller_male.plot_data.keys(), controller_female.plot_data.keys()))
    total_male_data = len(df[df['What is your Gender?'] == 'Male'])
    total_female_data = len(df[df['What is your Gender?'] == 'Female'])
    male_data = []
    female_data = []
    for item in all_keys:
        male_data.append(controller_male.plot_data.get(item, 0))
        female_data.append(controller_female.plot_data.get(item, 0))
    male_data = (np.array(male_data) / total_male_data) * 100
    female_data = (np.array(female_data) / total_female_data) * 100
    barWidth = 0.25
    r1 = np.arange(len(all_keys))
    r2 = [x + barWidth for x in r1]

    # Make the plot
    plt.bar(r1, male_data, color='#7f6d5f', width=barWidth, edgecolor='white', label='Male')
    plt.bar(r2, female_data, color='#557f2d', width=barWidth, edgecolor='white', label='Female')

    # Add xticks on the middle of the group bars
    # plt.xlabel('group', fontweight='bold')
    plt.ylabel('Frequency (%)', fontsize=32)
    plt.xticks([r + barWidth for r in range(len(all_keys))], all_keys)

    # Create legend & Show graphic
    plt.legend(prop={'size': 32})
    plt.show()
if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../data/government.csv")
    show_bar_plot(df, ExpectationFromGovernmentFigureController)


    df = pd.read_csv("../data/managers.csv")
    show_bar_plot(df, ExpectationFromManagersFigureController)


    df = pd.read_csv("../data/new_hires.csv")
    show_bar_plot(df, ExpectationFromNewHiresFigureController)


    df = pd.read_csv("../data/organization.csv")
    show_bar_plot(df, ExpectationFromOrganizationFigureController)


    df = pd.read_csv("../data/peers.csv")
    show_bar_plot(df, ExpectationFromPeersFigureController)


    df = pd.read_csv("../data/peers_employees.csv")
    show_bar_plot(df, ExpectationFromPeersEmployeesFigureController)


    df = pd.read_csv("../data/universities.csv")
    show_bar_plot(df, ExpectationFromGovernmentFigureController)


# female manager career opportunity
# male manager team player
#female peer employee sincerity, supportive
# female university job availability