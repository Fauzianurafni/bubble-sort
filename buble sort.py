from flask import Flask, render_template, request

Bs = Flask(__name__)

@Bs.route('/')
def index():
    return render_template('bubble-sort.html')

def bubble_sort(n, data):
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            if data[j] < data[j - 1]:
                tampung = data[j]
                data[j], data[j - 1] = data[j - 1], tampung
    return data

@Bs.route('/proses', methods=['POST'])
def proses():
    n = int(request.form['n'])
    data = [int(request.form[f'data{i}']) for i in range(1, n + 1)]
    sebelum_diurutkan = data[:]
    sesudah_diurutkan = bubble_sort(n, data)
    hasil = {'data': sebelum_diurutkan, 'sesudah_diurutkan': sesudah_diurutkan}
    return render_template('bubble-sort.html', hasil=hasil)

if __name__ == '__main__':
    Bs.run()
