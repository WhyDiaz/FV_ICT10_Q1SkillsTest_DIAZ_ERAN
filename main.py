from pyscript import document, display

def create_order(e):
    document.getElementById("Subtotal").innerHTML = "" 
    document.getElementById("VAT").innerHTML = ""
    document.getElementById("Total_Amount").innerHTML = ""

    math = document.getElementById('math') 
    mathprice = float(math.value) * math.checked

    ss = document.getElementById('ss')
    ssprice = float(ss.value) * ss.checked

    science = document.getElementById('science')
    scienceprice = float(science.value) * science.checked

    english = document.getElementById('english')
    englishprice = float(english.value) * english.checked

    filipino = document.getElementById('filipino')
    filipinoprice = float(filipino.value) * filipino.checked

    ve = document.getElementById('ve')
    veprice = float(ve.value) * ve.checked

    ict = document.getElementById('ict')
    ictprice = float(ict.value) * ict.checked

    cat = document.getElementById('cat')
    catprice = float(cat.value) * cat.checked

    music = document.getElementById('music')
    musicprice = float(music.value) * music.checked

    
    sub = mathprice + ssprice + scienceprice + englishprice + filipinoprice + veprice + ictprice + catprice + musicprice
    vat = sub * 0.12 
    total = vat + sub 

    Sub = f"Subtotal: ₱{sub:.2f}"
    display(Sub, target="Subtotal") 

    Vat = f"VAT (12%): ₱{vat:.2f}"
    display(Vat, target="VAT")

    Total = f"Total Amount: ₱{total:.2f}"
    display(Total, target="Total_Amount")

