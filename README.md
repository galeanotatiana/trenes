# Combinaciones de trenes de Buenos Aires

Script que analiza un grafo de todas las estaciones de trenes activas de Buenos Aires y busca el camino más corto (medido en cantidad de estaciones, no en tiempo de viaje) para llegar solo en tren. En caso de no existir una combinación, se informa por mensaje.

---

# Estado del proyecto
Este proyecto está en **desarrollo**.

# Ejemplos de uso
- Dessde La Plata hacia Lobos:
![Ejemplo La Plata - Lobos](/screenshots/ejemplo-1.png)

- Desde Retiro hacia Constitucion: informa que no hay conexión mediante tren.
![Ejemplo Constitucion - Retiro](/screenshots/ejemplo-2.png)

---

# Notas
- Aún no cuenta con horarios, tiempo de viaje ni interfaz.
- Ramales de larga distancia aún no incorporados.
- Los nombres de muchas estaciones están abreviados por simplicidad.
- El archivo .dot es un grafo dirigido, aunque el programa **lo interpreta como no dirigido**. De esta forma se pueden hacer los recorridos en ambos sentidos.

# Dependencias
- Python 3.12.3
- Graphviz 
- PyGraphviz (`pip install pygraphviz`)  
- NetworkX (`pip install networkx`)


