test = {
  'name': 'Call Expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from operator import add
          >>> def double(x):
          ...     return x + x
          >>> def square(y):
          ...     return y * y
          >>> def f(z):
          ...     add(square(double(z)), 1)
          >>> f(4)
          fef9a0b77f7c83478c249aedcc62186d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def foo(x, y):
          ...     print("x or y")
          ...     return x or y
          >>> a = foo
          fef9a0b77f7c83478c249aedcc62186d
          # locked
          >>> b = foo()
          9ee30c0bb2642a554fb2198e3b73feb1
          # locked
          >>> c = a(print("x"), print("y"))
          ff318045874bb7f788b2309eaa0f4894
          da02dee03c156475c7c29393dacfc3f5
          7ddbdb50919b472a75075471bd5596e5
          # locked
          >>> print(c)
          399369abd1b48a38479bd1bfa475106f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def welcome():
          ...     print('welcome to')
          ...     return 'hello'
          >>> def cs61a():
          ...     print('cs61a')
          ...     return 'world'
          >>> print(welcome(), cs61a())
          204ec822686298ee05e57f3c0b56b819
          0f528d2547869677927cf019eefdf1e0
          1047f769134a5d283d048fc7f113428e
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
