(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (rest) (append (cons first nil) rest)) rests))

(define (zip pairs)
  (define (zip-helper pairs lst1 lst2)
    (cond
      ((null? pairs) (list lst1 lst2))
      (else
        (define pair (car pairs))
        (zip-helper
          (cdr pairs)
          (append lst1 (list (car pair)))
          (append lst2 (list (cadr pair))))
      )
    )
  )
  (zip-helper pairs nil nil)
  )

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  ; inspect the first element and tack on the index value, then process the rest of the list
  (define (helper lst index)
    (if (null? lst)
      nil
      (cons
        (list index (car lst)) ; equal to "(index value)"
        (helper (cdr lst) (+ 1 index))) ; process the rest of the list with index + 1
    )
  )
  (helper s 0))
  ; END PROBLEM 17

; count-partitions implemented from section 1.7 reading
; only difference is that it uses a 'denoms' list to count the partitions
(define (count-partitions total denoms)
  (cond
    ((< total 0) 0)     ; the total can't be negative, thus we have an invalid partition
    ((null? denoms) 0)  ; no more denominations to use for splitting the total, thus we have an invalid partition
    ((= total 0) 1)     ; valid partition detected!
    (else
      (+
        ; subtract the total from the biggest denom and call count-partitions
        (count-partitions (- total (car denoms)) denoms)
        ; pop the biggest denom, since it's bigger than total, and call count-partitions
        (count-partitions total (cdr denoms))
      )
    )
  )
)

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  ; referencing the count_partitions function from reading section 1.7 ...
  ; we can use its general structure to solve any kind of partition-related problem
  ; the general rules goes as follows:
  ; - if the input number is negative, we don't have a proper partition
  ; - if there aren't enough parts to divide the input number (i.e. no denoms or it's less than 0),
  ;   we don't have a proper partition
  ; - if the input number is 0, we found a proper partition
  ; - otherwise, try the same function, but with 2 variations:
  ;   - subtract the input number by the biggest denomination available (we still have a possibly valid partition)
  ;   - pop the biggest denomination (or subtract it by 1 for count partitions) (we don't have a valid partition, but keep exploring)
  ; - combine the two results according to the requirements of the function

  ; new solution
  ; strat:
  ; - instead of having an extra variable to keep track of the current partition, we use the power
  ; - of cons-all to save the state of the current partition
  (cond
    ((< total 0) nil)     ; the total can't be negative, thus we have an invalid partition
    ((null? denoms) nil)  ; no more denominations to use for splitting the total, thus we have an invalid partition
    ((= total 0) (list nil))  ; valid partition detected: return a nested empty list (since cons-all appends to the beginning of the list,
                              ; it will be the end of the list and the numbers of the valid partition will be appended from right to left
    (else
      ; we use append to combine the null lists and the proper partitions, since append flattens
      ; all lists by one layer and adds them to a bigger list
      (append
        ; subtract the total from the biggest denom and call cons-all with the current denomination number to be added
        (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
        ; pop the biggest denom, since it's bigger than total, and call this function again
        (list-change total (cdr denoms))
      )
    )
  )

  ; old solution
  ; strat:
  ; - 'curr' holds a possibly valid partition
  ; - recursively interate through all partitions similar to the count_partitions technique, except we have
  ;   a given list of denominations in place of a number to represent the parts available to divide the total,
  ;   and we are returning a list of possible partitions instead of the number of partitions
  ; (define (helper total denoms curr)
  ;   (cond
  ;     ((< total 0) nil)     ; the total can't be negative, thus we have an invalid partition
  ;     ((null? denoms) nil)  ; no more denominations to use for splitting the total, thus we have an invalid partition
  ;     ((= total 0) (list curr)) ; return 'curr' (a valid partition) encapsulated in a list itself (see below why)
  ;     (else
  ;       ; we use append to combine the null lists and the proper partitions, since append flattens all lists by one layer
  ;       ; and adds them to a bigger list (hence why 'curr' is encapsulated by a list when a valid partition is found)
  ;       (append
  ;         ; subtract the total from the biggest denom and add the latter number to 'curr'
  ;         (helper (- total (car denoms)) denoms (append curr (list (car denoms))))
  ;         ; pop the biggest denom, since it's bigger than total, and call this function again
  ;         (helper total (cdr denoms) curr)
  ;       )
  ;     )
  ;   )
  ; )

  ; (helper total denoms nil)
  )
  ; END PROBLEM 18


;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr ; leave it alone, since it's just a value
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr ; leave it alone, since it's most likely a special symbol (like 'lambda or 'let)
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))    ; either 'lambda or 'define (most likely the former)
               (params (cadr expr))   ; all the parameters that the lambda function requires
               (body   (cddr expr)))  ; the body of the lambda expression
           ; BEGIN PROBLEM 19
           (cons form (cons params (map let-to-lambda body))) ; merge all three together, making sure that the body has no let statements
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (define zipped (zip values))   ; we zip the values to separate the variables and their respective values in 2 lists
           (define vars (car zipped))     ; the parameters the lambda function can take
           (define vals (map let-to-lambda (cadr zipped)))  ; the values to pass into the lambda after removing any let statements
           (define processed-body (map let-to-lambda body)) ; the body of the lambda, after removing any let statements
           (cons (append (list 'lambda vars) processed-body) vals) ; merge them all! format: ((lambda vars processed-body) vals)
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr) ; just process each part of the expression with let-to-lambda, since it's probably a "deep" expression
         ; END PROBLEM 19
         )))
