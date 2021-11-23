# spherical_filtration
## Modeling the moving of fluid to the wellbores of wells with different constructure using the spherical filtration.


---

* Сopy your **.xlsx** file to appropriate folder
where the **.exe** file locates. In sended archive there is a test-file with the number of
wells and data called *list_wells_test.xlsx*
* When you started to use **.exe** file print the **name** of your **.xlsx** file in input 
empty field like *list_wells_test.xlsx* and press the *Импортировать* button.
* File is ready for processing. Now you can press the *ВЫПОЛНИТЬ РАСЧЕТ* button. In the following
empty field the total **oil rate (surface conditions), m^3/day** will appear.
* Press buttons only **once**!
* Check that in excel-file column names are similar to column names in test file:
  * name of the column with the well number: *'Well'*
  * name of the column with the value of the reservoir pressure: *'Reservoir pressure, atm'*
  * name of the column with the value of the wellbore pressure: *'Wellbore pressure, atm'*
  * name of the column with the value of oil viscosity: *'Oil viscosity in reservoir conditions, cP'*
  * name of the column with the volume factor: *'Fvf, m3/m3'*
  * name of the column with the value of effective thickness: *'Effective thickness, meters'*
  * name of the column with the value of reservoir permeability: *'Permeabillity, mD'*
  * name of the column with the value of well radius: *'Well radius, m'*
  * name of the column with the value of supply contour radius: *'Supply contour radius, m'*
  * name of the column with the value of formation thickness: *'Formation thickness, m'*
  * name of the column with the distance from unit to the bottom of the formation: *'Run to the bottom of formation, m'*
  * name of the column with the value of the distance between units: *'Distance between spheres, m'*
* Press the  *Экспортировать* button and get a new **.xlsx** file called *solution.xlsx*!
* Good luck!


---


* Cкопируйте ваш файл с расширением **.xlsx** в соответствующую
папку, где располагается файл с приложением формата **.exe**. В отправленном архиве
находится файл с несколькими скважинами-узлами и данными по ним под названием *list_wells_test.xlsx*
* Когда вы запустили **.exe** файл, то первым делом введите в пустое поле для ввода текста название своего **.xlsx** файла, к примеру
нашего тестового файла *list_wells_test.xlsx* и нажмите кнопку *Импортировать*
* Файл готов к обработке. Теперь вы можете нажать кнопку *ВЫПОЛНИТЬ РАСЧЕТ*. После ее нажатия программа обработает
импортированный **.xlsx** файл и в пустом поле под кнопкой выведет значение суммарного дебита в посерхностных условиях 
по всем узлам в м^3/сут. 
* Нажимайте кнопки только **один раз!**
* Проверьте, что названия столбцов в excel-файле такие же, как в нашем тестовом файле:
  * название столбца с номером скважины: *'Well'*
  * название столбца с пластовым давлением: *'Reservoir pressure, atm'*
  * название столбца с забойным давлением: *'Wellbore pressure, atm'*
  * название столбца со значениями динамической вязкости: *'Oil viscosity in reservoir conditions, cP'*
  * название столбца с объемным коэффициентом: *'Fvf, m3/m3'*
  * название столбца с эффективной толщиной: *'Effective thickness, meters'*
  * название столбца с проницаемостью: *'Permeabillity, mD'*
  * название столбца с радиусом скважины: *'Well radius, m'*
  * название столбца со значением радиуса конутра питания: *'Supply contour radius, m'*
  * название столбца со значение толщины коллектора: *'Formation thickness, m'*
  * название столбца с расстоянием от узла до подошвы пласта: *'Run to the bottom of formation, m'*
  * название столбца с расстоянием между узлами: *'Distance between spheres, m'*
* Нажмите кнопку  *Экспортировать*, тогда в вашей папке появится новый **.xlsx** файл под навзанием *solution.xlsx*!
* Удачи!