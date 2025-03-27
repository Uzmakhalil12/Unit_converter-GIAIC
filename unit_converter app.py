import streamlit as st
def convert_units( value:float,unit_from:str,unit_to:str):
    # print("value>>>",value)
    # print("unit_from>>>",unit_from)
    # print("unit_to>>>",unit_to)
    
    # 1 kilometer=1000 meters
    # 1 meter=0.001 kilometers
    # 1 kilometer=1000 grams
    # 1 gram=0.001 kilogram

    if unit_from=="kilometers"and unit_to=="meters":
        # 1.5*1000
        return value * 1000
    
    elif unit_from=="meters"and unit_to =="kilometers":
        return value* 0.001
    elif unit_from=="kilograms"and unit_to=="grams":
        return value*0.001
    else:
        return "coversion is not supported"

    # result=output ki value
    
result1 =convert_units(1.5,"kilometers","meters")
print("result value is", result1)
result2 =convert_units(5000,"meters","kilometers")
print("result value is", result2)
result3 =convert_units(1.5,"kilograms","grams")
print("result value is", result3)

def main():
    st.title("unit_ converter")
    st.write("welcome to unit converter")
    value=st.number_input("enter the value you want to convert:")
    unit_to=st.text_input("enter the unit you want to convert from(meters, kiolograms,grams)")
    unit_from=st.text_input("enter the unit you want from conversion (meters, kilograms,grams)")
    if st.button("convert"):
        result = convert_units(value,unit_to,unit_from)
        st.write("converted value is:", result)

    # print ("unit converter") 
    # print("welcome to unit converter!")

    # value= float(input("enter the value you want to convert:")) # 1  -> 1.5 ->
    # unit_to=input("enter the unit you want to convert from(meters, kiolograms,grams)")
    # unit_from=input("enter the unit you want from conversion (meters, kilograms,grams)")

    # print ("value>>>",value)
    # print ("unit_to>>>",unit_to)
    # print ("unit_from>>>",unit_from)
    # result = convert_units(value,unit_to,unit_from)
    # print("converted value is",result)
main()
