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
            // console.log(data);
            objectManager.add(data);
        });
}

function btnClicked(){
    const textHeight = document.getElementById('input-height')
    const textRainny = document.getElementById('input-rainny')
    const textNitrogen= document.getElementById('input-nitrogen')
    const textSunny= document.getElementById('input-sunny')
    const textTransport= document.getElementById('input-transport')

    console.log(textHeight.value)
    console.log(textRainny.value)
    console.log(textNitrogen.value)
    console.log(textSunny.value)
    console.log(textTransport.value)
};

setTimeout(()=>{
    const btnOk = document.getElementById('btn-ok');

    btnOk.addEventListener('click', ()=>{
        btnClicked()
    });
}, 1000);
