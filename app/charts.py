import matplotlib.pyplot as plt

def generate_bar_char(labels,values):
    
    fig,ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig('bar.png')
    plt.close()

def generate_pie_chart(name, labels,values):
    fig,ax= plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.savefig(f'./img/{name}.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [100,200,300]
    #generate_bar_char(labels, values)
    generate_pie_chart(labels,values)