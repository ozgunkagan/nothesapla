import streamlit as st

# Sitenin Başlığı
st.title("🎓 Üniversite Not Hesaplama Aracı")
st.write("Ders notlarını aşağıya gir, geçip geçmediğini hemen öğren!")

# Ekranı iki sütuna bölelim (daha şık dursun diye)
col1, col2 = st.columns(2)

with col1:
    participation = st.number_input("Participation (0-100)", min_value=0.0, max_value=100.0)
    Presentation = st.number_input("Presentation (0-100)", min_value=0.0, max_value=100.0)
    Impromptu_Speech = st.number_input("Impromptu Speech (0-100)", min_value=0.0, max_value=100.0)
    RD_Quiz = st.number_input("RD Quiz (0-100)", min_value=0.0, max_value=100.0)

with col2:
    MC_Quiz = st.number_input("MC Quiz (0-100)", min_value=0.0, max_value=100.0)
    Book_Assignments = st.number_input("Book Assignments (0-100)", min_value=0.0, max_value=100.0)
    Midterm = st.number_input("Midterm (0-100)", min_value=0.0, max_value=100.0)
    Final = st.number_input("Final (0-100)", min_value=0.0, max_value=100.0)

# Hesaplama Butonu
if st.button("Sonucumu Hesapla"):
    
    # Senin hesaplama kodların aynen burada:
    not_participation = participation * 0.1
    not_Presentation = Presentation * 0.025
    not_Impromptu_Speech = Impromptu_Speech * 0.025
    not_RD = RD_Quiz * 0.05
    not_MC = MC_Quiz * 0.05
    not_Book = Book_Assignments * 0.05
    not_Midterm = Midterm * 0.3
    not_Final = Final * 0.4

    toplam_not = (not_participation + not_Presentation + not_Impromptu_Speech + 
                  not_RD + not_MC + not_Book + not_Midterm + not_Final)

    st.divider() # Araya çizgi çeker

    # Senin mantık kuralların (Düzeltilmiş haliyle):
    if Final < 50:
        if toplam_not >= 60:
            st.error(f"🔴 KALDINIZ! Ortalamanız tutuyor ama Final barajına takıldınız. (Final: {Final})")
            st.info(f"Genel Ortalamanız (GPA): {toplam_not:.2f}")
        else:
            st.error(f"🔴 KALDINIZ! Hem Final barajı hem de ortalama yetersiz.")
            st.write(f"Genel Ortalamanız (GPA): {toplam_not:.2f}")

    elif toplam_not < 60:
        st.error(f"🔴 KALDINIZ! Finaliniz iyi ama ortalamanız 60'ın altında.")
        st.write(f"Genel Ortalamanız (GPA): {toplam_not:.2f}")

    else:
        st.success(f"🟢 TEBRİKLER GEÇTİNİZ!")
        st.balloons() # Ekranda balonlar uçuşur :)
        st.write(f"Genel Ortalamanız (GPA): {toplam_not:.2f}")