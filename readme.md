# Proyecto I. Computo Paralelo y Distribuido

Aplicar el MPI para la solución de problemas en Paralelo:

* QuickSort
* Binary search
* Web Scraping

### Pre requerimientos

* Python3

* build-essential 

* python3-dev

* mpich

``` bash
apt install build-essential python3-dev mpich
``` 

* mpi4py

``` bash
pip install mpi4py
```

## Comienzo

``` bash
pip install -r requirements.txt
```



### Run web scrapping

``` bash
mpiexec -n 4 python web_scrapping.py
```