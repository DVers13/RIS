import matplotlib.pyplot as plt
from datetime import timedelta


class SchuhartControlCard:

    def __init__(self, data):
        self.data = data
        self.x = None
        self.x_u_cl = None
        self.x_l_cl = None
        self.r = None
        self.r_u_cl = None
        self.r_l_cl = 0

    def fix_date(self):
        for idx in range(1, len(self.data['Дата'])):
            if self.data['Дата'][idx] <= self.data['Дата'][idx - 1]:
                self.data['Дата'][idx] += (self.data['Дата'][idx - 1] -
                                           self.data['Дата'][idx] +
                                           timedelta(days=2))

    def calculate_card(self):
        self.fix_date()
        self.x = self.data.loc[:, 'Сумма'].mean()
        new_R = [0]
        for i in range(1, len(self.data['Сумма'])):
            new_R.append(abs(self.data['Сумма'][i] -
                             self.data['Сумма'][i - 1]))
        self.data['R'] = new_R
        self.r = self.data.loc[1:, 'R'].mean()
        self.x_u_cl = self.x + 2.66 * self.r
        self.x_l_cl = self.x - 2.66 * self.r
        self.r_u_cl = 3.267 * self.r
        print(f'Хср: {self.x}')
        print(f'Верхняя контрольная граница: {self.x_u_cl}')
        print(f'Нижняя контрольная граница: {self.x_l_cl}')
        print(f'Rm: {self.r}')
        print(f'Верхняя контрольная граница: {self.r_u_cl}')
        print(f'Нижняя контрольная граница: {self.r_l_cl}')

    def draw_card(self, name_table):
        w = 16.60
        h = 4.80
        fig, ax = plt.subplots()
        fig.set_size_inches(w, h)
        ax.plot(self.data['Дата'], self.data['Сумма'], 'o-', linewidth=2)
        ax.plot(self.data['Дата'], [self.x for _ in range(
            len(self.data['Дата']))])
        ax.plot(self.data['Дата'], [self.x_u_cl for _ in range(
            len(self.data['Дата']))])
        ax.plot(self.data['Дата'], [self.x_l_cl for _ in range(
            len(self.data['Дата']))])
        ax.legend(['Сумма', 'Среднее', 'U_cl',
                   'L_cl'], loc='center left',
                  bbox_to_anchor=(1, 0.5))
        save_name_x = f'images/Карта_индивидуальных_значений_{name_table}.png'
        plt.savefig(save_name_x)

        fig, ax = plt.subplots()
        fig.set_size_inches(w, h)
        ax.plot(self.data['Дата'][1:], self.data['R'][1:], 'o-',
                linewidth=2)
        ax.plot(self.data['Дата'][1:], [self.r for _ in range(
            len(self.data['Дата'][1:]))])
        ax.plot(self.data['Дата'][1:], [self.r_u_cl for _ in range(
            len(self.data['Дата'][1:]))])
        ax.plot(self.data['Дата'][1:], [self.r_l_cl for _ in range(
            len(self.data['Дата'][1:]))])
        ax.legend(['R', 'Среднее', 'U_cl',
                   'L_cl'], loc='center left',
                  bbox_to_anchor=(1, 0.5))
        save_name_r = f'images/Карта_скользящий_размахов_{name_table}.png'
        plt.savefig(save_name_r)
