
class Preprocessor:
    """
        This class shall  be used to clean and transform the data before training.
        Written By:Hardik Patel
        """

    def int_to_categorical(self, data):
        self.data = data
        try:
            cleanup1 = {1 : 'LB(L900-L1800)', 2 : 'SAA Alarm_BCCH Freq change_T200S_Down tilt', 3 : 'SD Assignment/T200S',
                        4 : 'Seems TRX Down', 5 : 'Seems TRX Down_Alarm', 6 :'Seems TRX Down_LB(L1800-L900)',
                        7 : 'Seems TRX Down_LB(L900-L1800)'}
            self.data.replace(cleanup1, inplace = True)
            print('Remarks are converted to categorical data')
            return self.data
        except Exception as e:
            print('Exception message % s' % e)
            raise Exception()

