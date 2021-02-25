1. Python interpreted bir dildir. İnterpreted dilin iş prinsipini izah edin:
    - Kodları sətir-sətir oxuyur. Koddakı error-a qədər işləyir və error yerində dayanır. Buna görə kodlardakı error-un hansı sətirdə olduğunu görə bilirik asanlıqla. 

2. Interpreted və compiler dillər arasında olan fərqləri izah edin:
    - İnterpreted dillər kodu sətir-sətir oxuyur; error-a qədər icra edir; kodu analiz edib işləyir.
    - Compiler dillər kodun hamısını oxuyur; error varsa işləmir; kodu analiz edir, sonra maşın dilinə çevirib icra edir.

3. Python data tipləri hansılardır? Hər biri haqqında qısa izahat verin:
    - str (string) - Mətn tipi - cümlə, ifadə, ad, soyad və s. daxil etmək üçün istifadə olunur. 
    - int və float - Ədəd tipi - int tam ədədlər üçün, float isə tam+kəsr hissəsi olanlar üçün.
    - bool - Boolean tipi - yalnız 2 dəyər ala bilir: TRUE və FALSE.
    - list, tuple, range - Sıra tipi - list elementləri array-e yığır; tuple mötərizədə yığır və dəyişdirilə bilmir; range dəyərləri aralıq kimi daxil etməyə imkan verir.


4. Object Oriented Programming nədir? Niyə belə bir paradigmanın var olduğunu izah edin:
    - Funksiyaları və dəyərləri bir obyektə yığır və kənar müdaxilə və yanlış istifadədən qoruyur.
    - Object Oriented Programming-in əsas elementləri class və obyektdir. 

5. Proqram yazarkən metodlardan istifadə edirik. Hansı hallarda metod istifadə edilməlidir?
    - Hazır metodlardan istifadə həm kodu qısaltmış olur, həm də daha asan olur. Buna görə ehtiyac olan hallarda istifadə edə bilərik. 

6. local və global variable nədir izah edin:
    - Əgər variable-ı function-un içində təyin etsək, o ancaq həmin function daxilində işləyəcək və başqa function-larda istifadə edə bilməyəcəyik - bu local variable-dır. 
    - Global variable isə function-dan əvvəl təyin olunur və istənilən function-da (bütün kod boyunca istənilən yerdə) istifadə oluna bilər.

7. Python type conversion haqqında izahat verin:
    - 2 növü var: Implicit ə Explicit. 
    - Implicit default verilən növdü. Məsələn: x=6 - int, a=3.9 - float və s.
    - Explicit manually dəyişdirilən növdü. Məsələn, x=6; x=str(x)  və s.

8. init nədir?
    - Constructordur və məlumatları yığmaq üçün ilkin parametrləri ala bilirik.

9. self nədir?
    - self hər obyektin atributları və metodları olmasına şərait yaradır.

10. *args,*kwargs nədir? nə zaman istifadə olunur?
    - Funksiyaya dəyişənli və ya dəyişənsiz arqument ötürmək üçün istifadə olunur. 

11. Python module nədir?
    - Python modulu .py extension-lı olan fayllardır. İçində dəyişənlər, function-lar və s. olur. 

12. Python package nədir?
    - Python modullarının meneceridir.

13. pass nədir? Nə zaman istifadə olunur?
    - Kodu boş saxlayıb sonra yazmaq istəyiriksə pass istifadə edirik. Boş saxlayanda error verir. 

14. List metodlarından 5 ədəd metodun izahatını yazın
    - sort() - siyahını sıralayır.
    - append() - siyahıya element əlavə etmək üçün istifadə olunur. 
    - count() - hər hansı elementin sayını tapır.
    - reverse() siyahını tərsinə çevirir.
    - min,max - siyahıda ən böyük və ən kiçik ədədi tapır. 

15. List və dict hansı hallarda istifadə olunur?
    - Məlumatları siyahıya almaq lazım gəldikdə list, key value-larla əlavə etmək lazım gəldikdə dict istifadə olunur. 

16. Dict metodlarından 5 ədəd metodun izahatını yazın
    - clear() - dict-in bütün elementlərini silir.
    - values() - dict-in value-larının listini qaytarır.
    - pop() - verilən key ilə elementi silir.
    - update() - verilən key ilə siyahını update edir. 
    - get() - Verilən açarin dəyərini qaytarır. 