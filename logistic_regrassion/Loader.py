class Loader:

    '''
    loads a csv file as a dataset.
    the file consists of number values, either integer of floating point, representing each feature
    '''

    @staticmethod
    def load_dataset(filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        # 8ewrw oti pairnw csv arxeia sta opoia ka8e paradeigma vrisketai se diaforetiki grammi
        # kai oti t paradeigmata apotelountai apo katigorikes idiotites
        # epipleon ola ta paradeigmata exoun ton idio ari8mo idiotitwn ek twn opoiwn i teleutaia einai i apokrisi


        # dimiourgw enan pinaka pinakwn me tis pi8anes times ka8e attribute.
        # parallila dimiourgw kai t dianismata twn paradeigmatwn.
        dataset = []
        for line in lines:
            attributes = line.split(sep = ',')
            data = []
            for a in attributes:
                a.strip()

                try:
                    attr = float(a)
                except ValueError:
                    try:
                        attr = int(a) # euxomai na ka
                    except ValueError:
                        attr = a

                data.append(attr)

            dataset.append(data)

        return dataset