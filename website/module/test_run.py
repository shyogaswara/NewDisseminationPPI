from main_module import deter_origin, _if_PGRVI_or_GSI, _if_KSI

if __name__ == '__main__':
    text_str_GSI = f'Info Gempa Mag:4.3 SR, 25-Feb-22 08:50:31 WIB, Lok:0.15 LU,99.96 BT (8 km BaratDaya TALU-PASAMANBARAT-SUMBAR), Kedlmn:3 Km ::BMKG-GSI'
    text_str_PGRVI = f'Info Gempa Mag:4.3, 25-Feb-22 08:50:31 WIB, Lok:0.15 LU,99.96 BT (8 km BaratDaya TALU-PASAMANBARAT-SUMBAR), Kedlmn:3 Km ::BMKG-PGR VI'
    text_str_KSI = f'Info Gempa Mag:4.3, 25-Feb-22 08:50:31 WIB,Lok: 0.15 LU - 99.96 BT (8 km BaratDaya TALU-PASAMANBARAT-SUMBAR), Kedlmn:3 Km ::BMKG-KSI'

    param, origin = deter_origin(text_str_KSI)

    if origin == 'BMKG-PGR VI' or origin == 'BMKG-GSI':
        eq_param = _if_PGRVI_or_GSI(param)
    elif origin =='BMKG-KSI':
        eq_param = _if_KSI(param)

    print(origin)
    print(eq_param)

