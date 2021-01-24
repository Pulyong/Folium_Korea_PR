import folium
import scrap_url

def create_marker(pr_list): # 마커 생성 & popup 내용
    city_names = list(pr_list.keys())
    locations = list(pr_list.values())
    
    for i in range(len(pr_list)): # popup에 가져올 내용
        html = f"""
        <h1 style="text-align:center; color: #e55934">{match_list[i][0]}</h1>
        <p style="text-align:center; font-size:27px; color:#f9a03f" >
        Enjoy the beautiful Korea through Youtube!!
        </p>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/{match_list[i][1]}" frameborder="0" allow="accelerometer;
         autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """
        # 마커 생성
        folium.Marker(
            locations[i],
            tooltip=f"<h4>Introducing the beautiful city of <b>{city_names[i]}</b></h4>",
            popup=html).add_to(m)

pr_list = {"SEOUL":[37.55997841731841, 126.97529766418414],
            "BUSAN":[35.14854620239508, 129.12981211447476],
            "JEONJU":[35.81545662436752, 127.15346127143155],
            "ANDONG":[36.53914372213846, 128.51817368516137],
            "MOKPO":[34.781394296973474, 126.38328745213919],
            "GANGNEUNG":[37.691611597754395, 129.032888716986]}
m = folium.Map(location=[36.62944750812678, 127.88883613608986],zoom_start=8)
match_list = scrap_url.run()
create_marker(pr_list)
m.save("Korea PR.html")