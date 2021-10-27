class PlotLayout:
    def __init__(self,
        plt, total_num, num_per_col=None, num_per_row=None,
        row_width = 5,
        col_width = 5,
    ) -> None:
        self.plt = plt
        self.total_num = total_num
        self.num_per_col = num_per_col
        self.num_per_row = num_per_row
        self.row_width = row_width
        self.col_width = col_width
        if num_per_row and num_per_col is None:
            self.row_num = total_num // num_per_row + total_num % num_per_row
            self.col_num = num_per_row
        elif num_per_col and num_per_row is None:
            self.row_num = num_per_col
            self.col_num = total_num // num_per_col + total_num % num_per_col
        else:
            raise Exception
        print(f"allocating {self.row_num} rows x {self.col_num} cols for {total_num} subplots.")
        
    def prepare(self):
        self.plt.figure(figsize=(self.col_num * self.col_width, self.row_num * self.row_width))

    def subplot(self, idx):
        return self.plt.subplot(self.row_num, self.col_num, idx + 1)
