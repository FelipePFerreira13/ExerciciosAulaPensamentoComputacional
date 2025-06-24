from database.database_tools import session
from database.database import Predio, Apartamento

class Cadastro_base:
    if session.query(Predio).count() == 0:
        # Adiciona 10 prédios fictícios
        predios = [
            Predio(rua="Rua das Palmeiras", numero="101", bairro="Centro", cidade="Novo Hamburgo", estado="RS"),
            Predio(rua="Av. Brasil", numero="202", bairro="Trindade", cidade="Novo Hamburgo", estado="RS"),
            Predio(rua="Rua das Flores", numero="303", bairro="Estreito", cidade="Novo Hamburgo", estado="RS"),
            Predio(rua="Rua do Sol", numero="404", bairro="Ingleses", cidade="Novo Hamburgo", estado="RS"),
            Predio(rua="Rua do Mar", numero="505", bairro="Campeche", cidade="Novo Hamburgo", estado="RS"),
            Predio(rua="Rua das Árvores", numero="606", bairro="Itacorubi", cidade="Floripa", estado="RS"),
            Predio(rua="Rua do Lago", numero="707", bairro="Córrego Grande", cidade="Floripa", estado="SC"),
            Predio(rua="Rua do Campo", numero="808", bairro="Pantanal", cidade="Floripa", estado="SC"),
            Predio(rua="Rua das Pedras", numero="909", bairro="Saco dos Limões", cidade="Floripa", estado="SC"),
            Predio(rua="Rua do Parque", numero="1001", bairro="Agronômica", cidade="Floripa", estado="SC"),
        ]

        for predio in predios:
            session.add(predio)
        session.commit()

        # Adiciona um apartamento para cada prédio, com valores diferentes e link_google
        apartamentos = [
            Apartamento(
                id_predio=predios[0].id, numero_apartamento="11", valor=180000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[1].id, numero_apartamento="22", valor=210000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[2].id, numero_apartamento="33", valor=195000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[3].id, numero_apartamento="44", valor=250000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[4].id, numero_apartamento="55", valor=170000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[5].id, numero_apartamento="66", valor=230000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[6].id, numero_apartamento="77", valor=200000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[7].id, numero_apartamento="88", valor=260000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[8].id, numero_apartamento="99", valor=175000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
            Apartamento(
                id_predio=predios[9].id, numero_apartamento="101", valor=220000.00,
                link_google=f"https://www.google.com/maps/place/Condom%C3%ADnio+Plaza+Eldorado/@-29.6842675,-51.1253589,3a,75y,185.74h,120.23t/data=!3m7!1e1!3m5!1s7uELbxGisqhTTJHNDZY7zQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D-30.229758773473932%26panoid%3D7uELbxGisqhTTJHNDZY7zQ%26yaw%3D185.73830019023447!7i16384!8i8192!4m6!3m5!1s0x951943b04c37b9ed:0x8a0cc72cc9e8be12!8m2!3d-29.6843687!4d-51.1253123!16s%2Fg%2F1td59slq?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D"
            ),
        ]

        for ap in apartamentos:
            session.add(ap)
        session.commit()
