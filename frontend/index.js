ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [43.58, 39.72],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32,
            clusterDisableClickZoom: true
        });

    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.clusters.options.set('preset', 'islands#greenClusterIcons');
    myMap.geoObjects.add(objectManager);

    fetch('http://0.0.0.0:8000/all-dots/yandex_format/?limit=10')
        .then((response)=>{
            return response.json();
        })
        .then((data)=>{
            console.log(data);
            objectManager.add(data);
        });

}