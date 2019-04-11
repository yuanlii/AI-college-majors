import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class UnemployedAnalysis(object):
    '''this class is used for analyze unemployment data'''
    def __init__(self):
        self.data = pd.Series()
        self.cols = []
        self.unemploy_by_majorCat = pd.Series()
        self.major_category_data_dct = {}

    def load_data(self,input_data_path):
        self.data = pd.read_csv(input_data_path)
        self.cols += self.data.columns.unique().tolist()
        return self.data

    def plot_unemployment_rate_distribution(self, data):
        '''plot distribution for unemployment rate of each major_category '''
        major_categories = data['Major_category'].unique().tolist()
        print('there are %d unique major categories'% len(major_categories))
        print('unique major categories:')
        print(major_categories)
        print('---')

        # get subset df by "major_category"
        # major_category_data_dct = {}
        for major_category in major_categories:
            major_category_data = data[data['Major_category'] == major_category]
            self.major_category_data_dct[major_category] = major_category_data

        # plot distribution for each class
        plt.figure(figsize = (12,12))
        for i in range(len(major_categories)):
            plt.subplot(4, 4, i+1)
            plt.subplots_adjust(top = 0.99, bottom=0.1, hspace=0.5, wspace=0.3)
            unemployed = self.major_category_data_dct[major_categories[i]].Unemployment_rate.values
            sns.distplot(unemployed)
            plt.title(major_categories[i])
        plt.show()
    
    def plot_unemployment_by_majorCat(self, data):
        '''plot bar chart: visualize each major category and its related unemployment rate'''
        # group by major category
        self.unemploy_by_majorCat = data[['Major_category','Unemployment_rate']].groupby('Major_category').mean()
        # sort by unemployment_rata
        self.unemploy_by_majorCat = self.unemploy_by_majorCat.sort_values(['Unemployment_rate'], ascending = False)
        # plot bar chart
        ax = sns.barplot(y = self.unemploy_by_majorCat.index.tolist(), x= self.unemploy_by_majorCat.Unemployment_rate, color="salmon", saturation=.5)
        ax.set_yticklabels(labels = self.unemploy_by_majorCat.index.tolist())
        ax.set_title('Average unemployment rate by major category')
        plt.show()

    def get_median_payment_by_majorCat(self, data):
        ''' get median payment of each major_category '''
        median_pay = data[['Major_category','Median']].groupby(['Major_category']).median()
        median_pay = median_pay.sort_values(['Median'], ascending = False)
        # plot bar chart
        ax = sns.barplot(y = median_pay.index.tolist(), x= median_pay.Median)
        plt.title('median earnings by major categories')
        plt.show()

    def get_major_by_majorCat(self,major_cat):
        '''get the majors of one major_category'''
        print('%s major category contains these majors:'% major_cat)
        majors = self.major_category_data_dct[major_cat].Major.unique().tolist()
        return majors

    def get_unemployment_by_major(self,data):
        '''get unemployment data of each major in each major_category '''
        unemployment_by_major = data[['Major','Major_category','Unemployment_rate']].groupby(['Major_category','Major']).mean()
        unemployment_by_major = unemployment_by_major.reset_index()
        return unemployment_by_major

    def sort_unemployment_in_majorCat(self,major_cat):
        '''input a major_category, output the unemployment rate of each major of the category sorted in desceding order '''
        unemployment_by_major = self.get_unemployment_by_major(self.data)
        sorted_unemployment_data = unemployment_by_major[unemployment_by_major['Major_category'] == major_cat].sort_values(['Unemployment_rate'],ascending=False)
        print('unemployment rate for each major in %s:' % major_cat)
        return sorted_unemployment_data


    
    

    

    


    



                

    
