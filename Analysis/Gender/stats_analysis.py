import pandas as pd
import numpy as np
import scipy.stats as ss

def get_contingency_table(table, row_name, column_name):
    a = table.loc[row_name][column_name]
    b = table.loc[row_name].drop(columns=[column_name]).sum().sum()
    c = table.drop(index=[row_name])[column_name].sum().sum()
    d = table.drop(index=[row_name]).drop(columns=[column_name]).sum().sum()
    return np.array([[a,b],[c,d]])

def stat_test_career():
    df = pd.read_csv("../../data/managers.csv")
    gender = []
    career_opportunity = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if row[1]['categories'].strip() == 'Career Opportunity':
                career_opportunity.append("Career Opportunity")
            else:
                career_opportunity.append("Others")

    new_df = pd.DataFrame({
        "gender": gender,
        "career": career_opportunity
    })
    contingency_table = pd.crosstab(new_df['gender'], new_df["career"])
    print(ss.chi2_contingency(get_contingency_table(contingency_table, 'Female', "Career Opportunity")))

def stat_test_team():
    df = pd.read_csv("../../data/managers.csv")
    gender = []
    team_player = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if row[1]['categories'].strip() == 'Team Player':
                team_player.append("Team Player")
            else:
                team_player.append("Others")

    new_df = pd.DataFrame({
        "gender": gender,
        "team": team_player
    })
    contingency_table = pd.crosstab(new_df['gender'], new_df["team"])
    print(ss.chi2_contingency(get_contingency_table(contingency_table, 'Male', "Team Player")))


def stat_test_peer_employee():
    df = pd.read_csv("../../data/peers_employees.csv")
    gender = []
    sincerity = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if row[1]['categories'].strip() in ['Sincerity','Supportive']:
                sincerity.append("Sincerity")
            else:
                sincerity.append("Others")

    new_df = pd.DataFrame({
        "gender": gender,
        "sincerity": sincerity
    })
    contingency_table = pd.crosstab(new_df['gender'], new_df["sincerity"])
    print(ss.chi2_contingency(get_contingency_table(contingency_table, 'Male', "Sincerity")))


def stat_test_university():
    df = pd.read_csv("../../data/government.csv")
    gender = []
    job = []
    for row in df.iterrows():
        if row[1]['What is your Gender?'] in ['Male', 'Female']:
            gender.append(row[1]['What is your Gender?'])
            if row[1]['categories'].strip() in ['Job Availability']:
                job.append('Job Availability')
            else:
                job.append("Others")

    new_df = pd.DataFrame({
        "gender": gender,
        "job": job
    })
    contingency_table = pd.crosstab(new_df['gender'], new_df['job'])
    print(ss.chi2_contingency(get_contingency_table(contingency_table, 'Female', 'Job Availability')))
if __name__ == '__main__':
    stat_test_university()