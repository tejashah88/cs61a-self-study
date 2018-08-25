(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((> x 0) 1)
    ((= x 0) 0)
    (else -1))
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 1) b)
    ((even? n)
      (square (pow b (/ n 2))))
    ((odd? n)
      (* b (pow b (- n 1))))
  )
)

(define (ordered? s)
  (if
    (null? (cdr s)) ; check if we are at the last element, we can assume that it's an ordered list
    True
    (if
      (>= (cadr s) (car s)) ; check if first < second
      (ordered? (cdr s))    ; call ordered on the rest of the list
      False)
  )
)

(define (nodots s)
  (cond
    ((null? s) nil)
    ((number? s) (cons s nil))
    ((number? (car s)) (cons (car s) (nodots (cdr s))))
    ; we don't check if (cdr s) is a number, since it has to be either nil or another list to be well formed
    (else (cons (nodots (car s)) (nodots (cdr s))))
  )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((> (car s) v) #f)
          ((= (car s) v) #t)
          (else (contains? (cdr s) v)) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

; old solution
; (define (in-range a v b) (and (> v a) (> b v)))

; (define (add s v)
;     (cond ((empty? s) (list v))
;           ((number? s) (cons s nil))
;           ((contains? s v) s)
;           ((empty? (cdr s)) (list (car s) v))
;           ((> (car s) v) (append (cons v nil) s))
;           ((in-range (car s) v (cadr s)) (append (list (car s) v) (cdr s)))
;           (else (append (cons (car s) nil) (add (cdr s) v)))
;           ))

(define (add s v)
    (cond ((empty? s) (list v))
          ((contains? s v) s)        ; this will be triggered for the whole list, thus short-circuiting to returning the OG list
          ((> (car s) v) (cons v s)) ; i.e: if the first element is greater than 'v', put 'v' right before the list
          (else (cons (car s) (add (cdr s) v))) ; move through the rest of the list
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          (else
            (define e1 (car s))
            (define r1 (cdr s))
            (define e2 (car t))
            (define r2 (cdr t))
            (cond
              ((= e1 e2) (cons e1 (intersect r1 r2))) ; only add the value one time and process the rest of the 2 lists
              ((< e1 e2) (intersect r1 t)) ; keeping sorting in mind, disregard the first element of 's'  and process the rest of the lists' elements
              ((> e1 e2) (intersect s r2)) ; keeping sorting in mind, disregard the first element of 't'
            )
          )
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          (else
            (define e1 (car s))
            (define r1 (cdr s))
            (define e2 (car t))
            (define r2 (cdr t))
            (cond
              ((= e1 e2) (cons e1 (union r1 r2))) ; only add the value one time and process the rest of the 2 lists
              ((< e1 e2) (cons e1 (union r1 t)))  ; keeping sorting in mind, add the first element of 's' and process the rest of the lists' elements
              ((> e1 e2) (cons e2 (union s r2)))  ; keeping sorting in mind, add the first element of 't' and process the rest of the lists' elements
            )
          )
          ))