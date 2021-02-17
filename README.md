# Выполнение тстового задания на вакансию QA-стажёр в QA Center of Excellence
### Решение задачи №1
  
<p>Программа Task_1, выполняет требуемые операции<br>
Тестирование функций Test_task_1<p\>
  
### Найденные несоответствия:
В ходе выполнения задания с помощью https://jsonformatter.curiousconcept.com/ были найдены некоторые несоответствия
  <table border="1">
   <tr>
    <th>Файл</th>
    <th>Ошибка</th>
    <th>Описание</th>
    </tr>
   <td rowspan="6">TestcaseStructure.json</td><td rowspan="6">Лишняя запятая</td><td><p>Строка 5:<br>"value": "",<br>Лишняя запятая в конце строки</td></tr>
   <tr></td><td><p>Строка 9:<br>"value": "",<br>Лишняя запятая в конце строки</td></tr>
   <tr><td><p>Строка 23:<br>"title": "Publish item",<br>Лишняя запятая в конце строки</td></tr>
   <tr><td><p>Строка 26:<br>"title": "Edit item",<br>Лишняя запятая в конце строки</td></tr>
   <tr><td><p>Строка 38:<br>"title": "Authorize user",<br>Лишняя запятая в конце строки</td></tr>
   <tr><td><p>Строка 41:<br>"title": "Restore password",<br>Лишняя запятая в конце строки</td></tr>
   <tr><td>Values.json</td><td>Ошибка в массиве со значениями</td><td><p>Нессответствие значений в файле Values.json со значениями конечного корректного файла StructureWithValues.json:<br>В корректном файле StructureWithValues.json в массиве хранятся значения:<br>id = 73, value = 345, title = 'SellerX'.<br>В файле Values.json значению id=73 присвоено value = 354, что в конечном файле не вызовает ожидаемого присвоения 'SellerX' к значению title<br>Для получения результата соответствующему ожидаемому, в файле Values.json заменить значение "value": 354 на "value": 345  </td></tr>
   

  </table>


### Задача №2
Решение в файле TaskTestData.md
                                                  
