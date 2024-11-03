"""
COMP.CS.100 Programming 1
Code template for tanssipelit assigment.
"""

SONG_RESULT = {'kappale1': 13.0, 'kappale2': 1.2, 'kappale3': 19.5, 'kappale4': 11.1, 'kappale5': 91.9, 'kappale6': 1.5, 'kappale7': 80.0, 'kappale8': 79.9, 'kappale9': 0.4}
def calculate_average(S):
    """
    first sum all the values
    2ndly average the sum values
    :param S:
    :return:
    """

    n=sum(S.values())
    average= n/ len(S)
    return (average)
def main():
    (calculate_average(SONG_RESULT))
main()




