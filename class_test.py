import pandas as pd
import numpy as np

class Nobel:

    def __init__(self, name, field, year):
        self.name = name
        self.field = field
        self.year = year

    def __str__(self):
        return "{} was the winner in the field of {} in {}".format(self.name, self.field, self.year)


W_Röntgen = Nobel('Rôntgen', 'Physics', "1901")
P_Zeeman = Nobel('Zeeman', 'Physics', "1902")
M_Curie = Nobel('Curie', 'Physics', "1903")
J_Henricus = Nobel('Henricus', 'Chemistry', "1901")
E_Fisher = Nobel('Fisher', 'Chemistry', "1902")
S_Arrhenius = Nobel('Arrhenius', 'Chemistry', "1903")
E_Adolf = Nobel('Adolf', 'Medicine', "1901")
R_Ross = Nobel('Ross', 'Medicine', "1902")
N_Ryberg = Nobel('Ryberg', 'Medicine', "1903")


WINNERS = [W_Röntgen, P_Zeeman, M_Curie, J_Henricus, E_Fisher, S_Arrhenius, E_Adolf, R_Ross, N_Ryberg]


def fill_dataframe(winners: list) -> pd.DataFrame():
    """
    insert Nobel winners values into a df

    Parameters
    ----------
    winners : list of Nobel winners

    Returns
    -------
    DF with winners values
    """
    nobel_df = pd.DataFrame(columns=winners[0].__dict__.keys())
    for id, winner in enumerate(winners):
        nobel_df.loc[id] = winner.__dict__.values()
    return nobel_df

df = fill_dataframe(WINNERS)

def random_winner(values: pd.DataFrame) -> pd.Series:
    """
    Select a random winner from the winners df
    I used the function random.randint to select
    a random index between 0 and the length of the df,
    and then select the value of this index using .loc

    Parameters
    ----------
    values : DF with the winners values

    Returns
    -------
    Pandas series of a random winner

    """
    random_index = np.random.randint(len(values))
    random_value = values.loc[random_index]
    return random_value

random = random_winner(df)
print(random)
