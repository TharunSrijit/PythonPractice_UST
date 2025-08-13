Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
1+2
3
2-1
1
2*3
6
4/2
2.0
4//2
2
4%2
0
5%2
1
print("hello")
hello
2**3
8
2*2*2
8
print('marian\'s"sessions 3 & 4'")
      
SyntaxError: unterminated string literal (detected at line 1)
print('marian\'s"sessions 3 & 4"')
      
marian's"sessions 3 & 4"
print('marian'+'COE')
      
marianCOE
print(5,'marian')
      
5 marian
print(5'marian')
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(5*'marian')
      
marianmarianmarianmarianmarian
print(r'marinan1\nmarian2')
      
marinan1\nmarian2
print(r'5*"marian"')
      
5*"marian"
c='marian'
      
c[0]
      
'm'
c[-1]
      
'n'
c[1]+c[2]+c[4]+c[3]+[5]+c[6]
      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c[1]+c[2]+c[4]+c[3]+[5]+c[6]
TypeError: can only concatenate str (not "list") to str
c[1]+c[2]
      
'ar'
len(c)
      
6
c[0]+c[1]+c[2]+c[4]+c[3]+c[5]+c[6]
      
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c[0]+c[1]+c[2]+c[4]+c[3]+c[5]+c[6]
IndexError: string index out of range
6c[0]+c[1]+c[2]+c[4]+c[3]+c[5]
      
SyntaxError: invalid decimal literal
c[0]+c[1]+c[2]+c[4]+c[3]+c[5]
      
'marain'
c[0]+c[1]+c[1]+c[2]+c[4]+c[5]
      
'maaran'
c[0]+c[1]+c[3]+c[2]+c[4]+c[5]
      
'mairan'
c[:]
      
'marian'
c[:5]
      
'maria'
c[::-1]
      
'nairam'
c[::2]
      
'mra'
c[:]+'COE'
      
'marianCOE'
c[2:10]
      
'rian'
c[:]*2
      
'marianmarian'
c[:4]**2
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    c[:4]**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
c[:4]*2
      
'marimari'
c[:4].upper()
      
'MARI'
c[:4].upper()+c[4::-1]
      
'MARIairam'
c.capitalize()
      
'Marian'
i=1
      
type(i)
      
<class 'int'>
f=2.3
      
type(f)
      
<class 'float'>
inf=float(i)
      
type(i)
      
<class 'int'>
print(inf)
      
1.0
c=4+4i
      
SyntaxError: invalid decimal literal
c=3+4j
      
type(c)
      
<class 'complex'>
a=1
      
b=2
      
a>b
      
False
int(a>b)
      
0
i=[6,7,8,9,10]
      
i[0]
      
6
i[-5]
      
6
Nums=[1,2,3,4,5]
      
nums.append(10)
      
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    nums.append(10)
NameError: name 'nums' is not defined. Did you mean: 'Nums'?
Nums.append(10)
      
print(Nums)
      
[1, 2, 3, 4, 5, 10]
Nums.insert(2.10)
      
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    Nums.insert(2.10)
TypeError: insert expected 2 arguments, got 1
Nums.insert(2,10)
      
print(Nums)
      
[1, 2, 10, 3, 4, 5, 10]
Nums.remove(10)
      
print(Nums)
      
[1, 2, 3, 4, 5, 10]
del Nums[5]
      
print(Nums)
      
[1, 2, 3, 4, 5]
del Nums[3:]
      
print(Nums)
      
[1, 2, 3]
Nums.pop()
      
3
Nums.append(3)
      
print(Nums)
      
[1, 2, 3]
Nums.pop(1)
      
2
print(Nums)
      
[1, 3]
Nums.extend([2,3,4,5,6])
      
print(Nums)
      
[1, 3, 2, 3, 4, 5, 6]
Num.del[1]
      
SyntaxError: invalid syntax
del Num[1]
      
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    del Num[1]
NameError: name 'Num' is not defined. Did you mean: 'Nums'?
Nums.pop(2)
      
2
print(Nums)
      
[1, 3, 3, 4, 5, 6]
Nums.pop(1)
      
3
print(Nums)
      
[1, 3, 4, 5, 6]
Nums.insert(1,2)
      
print(Nums)
      
[1, 2, 3, 4, 5, 6]
min(Nums)
      
1
max(Nums)
      
6
sum(Nums)
      
21
Nums.sort()
      
print(Nums)
      
[1, 2, 3, 4, 5, 6]
n=[2,1,4,3]
      
n.sort()
      
print(Nums)
      
[1, 2, 3, 4, 5, 6]
n.sort(reverse=True)
      
print(Nums)
      
[1, 2, 3, 4, 5, 6]
print(n)
      
[4, 3, 2, 1]
n.sort()
      
print(n)
      
[1, 2, 3, 4]
s=['Tech','Tvm','MARIAN']
      
min(s)
      
'MARIAN'
max(s)
      
'Tvm'
sum(s)
      
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    sum(s)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
str.sort()
      
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    str.sort()
AttributeError: type object 'str' has no attribute 'sort'
s,sort()
      
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s,sort()
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
s.sort()
      
print(s)
      
['MARIAN', 'Tech', 'Tvm']
s.sort(reverse=-1)
      
print(s)
      
['Tvm', 'Tech', 'MARIAN']
c=[2,'b','a',1]
      
min(c)
      
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    min(c)
TypeError: '<' not supported between instances of 'str' and 'int'
max(c)
      
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    max(c)
TypeError: '>' not supported between instances of 'str' and 'int'
sum(c)
      
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    sum(c)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
c.sort()
      
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
c.sort(revese=-1)
      
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    c.sort(revese=-1)
TypeError: sort() got an unexpected keyword argument 'revese'. Did you mean 'reverse'?
l=['a','A','Z','z']
      
l.sort()
      
print(l)
      
['A', 'Z', 'a', 'z']
l=['1a','2A','0z']
      
sort(l)
      
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    sort(l)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
l.sort()
      
l
      
['0z', '1a', '2A']
min(l)
      
'0z'
max(l)
      
'2A'
sum(l)
      
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    sum(l)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
t=(0,2,1,3)
      
t(3)
      
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
t[3]
      
3
t[2]
      
1
t.append(4)
      
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    t.append(4)
AttributeError: 'tuple' object has no attribute 'append'
min(t)
      
0
t.sort()
      
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
t
      
(0, 2, 1, 3)
t=(0,1,2,1,3,1)
      
t.count(1)
      
3
t=('a',1,'A',1,3,1)
      
t.count(1)
      
3
min(t)
      
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    min(t)
TypeError: '<' not supported between instances of 'int' and 'str'
max(t)
      
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'int' and 'str'
sum(t)
      
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    sum(t)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
t.count(a)
      
3
a
      
1
t.count('a')
      
1
s={4,2,1,3,1,3}
      
s
      
{1, 2, 3, 4}
s={0,2,1,3}
      
s[2]
      
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
s[3]
      
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    s[3]
TypeError: 'set' object is not subscriptable
min(s)
      
0
max(s)
      
3
s.count(1)
      
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    s.count(1)
AttributeError: 'set' object has no attribute 'count'
s.pop()
      
0
s.add(5)
      
s
      
{1, 2, 3, 5}
s.remove(2)
      
s
      
{1, 3, 5}
s.remove(6)
      
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    s.remove(6)
KeyError: 6
s
      
{1, 3, 5}
s={'a','B','A','b'}
      
s
      
{'a', 'b', 'B', 'A'}
min(s)
      
'A'
max(s)
      
'b'
s={1,2,3,4}
      
s
      
{1, 2, 3, 4}
s.append(1.1)
      
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    s.append(1.1)
AttributeError: 'set' object has no attribute 'append'
s.add(1,1)
      
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    s.add(1,1)
TypeError: set.add() takes exactly one argument (2 given)
s.add(1.1)
      
s
      
{1, 2, 3, 4, 1.1}
range(5)
      
range(0, 5)
list(range(5))
      
[0, 1, 2, 3, 4]
list(range(2,5))
      
[2, 3, 4]
list(range(0,10,3))
      
[0, 3, 6, 9]
list(range(0,12,3))
      
[0, 3, 6, 9]
list(range(0,13,3))
      
[0, 3, 6, 9, 12]
range('a',5)
      
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    range('a',5)
TypeError: 'str' object cannot be interpreted as an integer
a=0
      
b=30
      
c=3
      
range(a,b,c)
      
range(0, 30, 3)
list(range(a,b,c))
      
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
range()
      
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    range()
TypeError: range expected at least 1 argument, got 0
type(range(5))
      
<class 'range'>
list(range(2,15,3))
      
[2, 5, 8, 11, 14]
a=2
      
list(range(a,a+13,a+1))
      
[2, 5, 8, 11, 14]
a=range(1,10,2)
      
b=range(10,21,2)
      
l.add(a)
      
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    l.add(a)
AttributeError: 'list' object has no attribute 'add'
l.append(a)
      
l.append(b)
      
l
      
['0z', '1a', '2A', range(1, 10, 2), range(10, 21, 2)]
l.pop(0)
      
'0z'
l
      
['1a', '2A', range(1, 10, 2), range(10, 21, 2)]
l.pop(0)
      
'1a'
l.pop(0)
      
'2A'
l
      
[range(1, 10, 2), range(10, 21, 2)]
l.delete()
      
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    l.delete()
AttributeError: 'list' object has no attribute 'delete'
a=list(range(1,10,2))
      
b=list(range(10,21,2)

       )
...       
>>> c=[a,b]
...       
>>> c
...       
[[1, 3, 5, 7, 9], [10, 12, 14, 16, 18, 20]]
>>> k={1:a,2:a,2:1}
...       
>>> k[1]
...       
[1, 3, 5, 7, 9]
>>> k={1:'a',2:'a',2:1}
...       
>>> k
...       
{1: 'a', 2: 1}
>>> k[2]
...       
1
>>> 9999**9999
...       
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    9999**9999
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
>>> 999**999
...       
368063488259223267894700840060521865838338232037353204655959621437025609300472231530103873614505175218691345257589896391130393189447969771645832382192366076536631132001776175977932178658703660778465765811830827876982014124022948671975678131724958064427949902810498973271030787716781467419524180040734398996952930832508934116945966120176735120823151959779536852290090377452502236990839453416790640456116471139751546750048602189291028640970574762600185950226138244530187489211615864021135312077912018844630780307462205252807737757672094320692373101032517459518497524015120165166724189816766397247824175394802028228160027100623998873667435799073054618906855460488351426611310634023489044291860510352301912426608488807462312126590206830413782664554260411266378866626653755763627796569082931785645600816236891168141774993267488171702172191072731069216881668294625679492696148976999868715671440874206427212056717373099639711168901197440416590226524192782842896415414611688187391232048327738965820265934093108172054875188246591760877131657895633586576611857277011782497943522945011248430439201297015119468730712364007639373910811953430309476832453230123996750235710787086641070310288725389595138936784715274150426495416196669832679980253436807864187160054589045664027158817958549374490512399055448819148487049363674611664609890030088549591992466360050042566270348330911795487647045949301286614658650071299695652245266080672989921799342509291635330827874264789587306974472327718704306352445925996155619153783913237212716010410294999877569745287353422903443387562746452522860420416689019732913798073773281533570910205207767157128174184873357050830752777900041943256738499067821488421053870869022738698816059810579221002560882999884763252161747566893835178558961142349304466506402373556318707175710866983035313122068321102457824112014969387225476259342872866363550383840720010832906695360553556647545295849966279980830561242960013654529514995113584909050813015198928283202189194615501403435553060147713139766323195743324848047347575473228198492343231496580885057330510949058490527738662697480293583612233134502078182014347192522391449087738579081585795613547198599661273567662441490401862839817822686573112998663038868314974259766039340894024308383451039874674061160538242392803580758232755749310843694194787991556647907091849600704712003371103926967137408125713631396699343733288014254084819379380555174777020843568689927348949484201042595271932630685747613835385434424807024615161848223715989797178155169951121052285149157137697718850449708843330475301440373094611119631361702936342263219382793996895988331701890693689862459020775599439506870005130750427949747071390095256759203426671803377068109744629909769176319526837824364926844730545524646494321826241925107158040561607706364484910978348669388142016838792902926158979355432483611517588605967745393958061959024834251565197963477521095821435651996730128376734574843289089682710350244222290017891280419782767803785277960834729869249991658417000499998999
>>> 100/81
...       
1.2345679012345678
