<p><span style="font-weight: 400;">Решение:</span></p>
<p><span style="font-weight: 400;">Позитивное и негативное функциональное тестирование черного ящика, техникой разделения на классы эквивалентности.</span></p>
<p></p>
<p><span style="font-weight: 400;">Классы эквивалентности:</span></p>
<ol>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">0 - 100</span> <span style="font-weight: 400;">(скидка 1%)</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">100 - 200</span> <span style="font-weight: 400;">(скидка 3%)</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">200 - 500</span> <span style="font-weight: 400;">(скидка 5%)</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">500 - &infin;</span> <span style="font-weight: 400;">(скидка 10%)</span></li>
</ol>
<p></p>
<p><span style="font-weight: 400;">Исходя из классов получаем тесты:</span></p>
<p></p>
<p><span style="font-weight: 400;">позитивные:</span></p>
<p><span style="font-weight: 400;">[0] </span> <span style="font-weight: 400;">- начисляется ли скидка 1%</span></p>
<p><span style="font-weight: 400;">[99] </span> <span style="font-weight: 400;">- проверка соответствия с первым классом (1%)</span></p>
<p><span style="font-weight: 400;">[100]</span> <span style="font-weight: 400;">- определение отношения к классу (1% или 3%)</span></p>
<p><span style="font-weight: 400;">[199]</span> <span style="font-weight: 400;">- проверка соответствия со вторым классом (3%)</span></p>
<p><span style="font-weight: 400;">[200]</span> <span style="font-weight: 400;">- определение отношения к классу (3% или 5%)</span></p>
<p><span style="font-weight: 400;">[499]</span> <span style="font-weight: 400;">- проверка соответствия с третьим классом (5%)</span></p>
<p><span style="font-weight: 400;">[500]</span> <span style="font-weight: 400;">- определение отношения к классу (5% или 10%)</span></p>
<p><span style="font-weight: 400;">[501] </span> <span style="font-weight: 400;">- проверка соответствия с четвертым классом (10%)</span></p>
<p></p>
<p><span style="font-weight: 400;">негативные:</span></p>
<p><span style="font-weight: 400;">[-1]</span> <span style="font-weight: 400;">- проверка отрицательных значений</span></p>
<p><span style="font-weight: 400;">[$@#]</span> <span style="font-weight: 400;">- проверка спец символов</span></p>
<p><span style="font-weight: 400;">[dagfrt]</span> <span style="font-weight: 400;">- проверка букв</span></p>
<p><br /><br /><br /><br /></p>

