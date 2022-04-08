#Jquery jak użyc

## W nagłowku (HEAD umieszczamy):

\<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>

#Jquery składnia 

* Składnia: $(selector).action()

    * $ ->  jQuery
    * selector - [element przeszukiwania (link)](https://www.w3schools.com/jquery/jquery_ref_selectors.asp)
    * action - [akcja (link)](http://api.jquery.com/)
    * event -  [wydarzenie (link)](https://www.w3schools.com/jquery/jquery_events.asp)
* Przykłady:
    * $(this).hide() - ukrywa aktualny element
    * $("p").hide() - ukrywa wszystkie paragrafy \<p>
    * $("#bb").hide()  - ukrywa element o id="bb"
    * $(".klasa").hide() - ukrywa elementy klasy klasa

# Trzeba zadbac o synchronizacje 

Po to aby skrypt sie nie zaczał uruchamiać zanim strona sie załaduje w komplecie:


$(document).ready(function(){
   // jQuery methods go here...

}); 

