;; Extra Scheme Questions ;;


; Q5
; apparently the image from the spring 2018 website doesn't exist, but I found an equivalent one in the 2017 version
; originally downloaded from: https://inst.eecs.berkeley.edu/~cs61a/sp17/lab/lab09/assets/list2.png
(define lst
  '((1) 2 (3 . 4) 5)
)

; Q6
(define (composed f g)
  (lambda (input) (f (g input)))
)

; Q7
(define (remove item lst)
  (filter (lambda (e) (not (= e item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  ; copying the same strat from Lab 3
  (if (= b 0) a (gcd b (modulo a b)))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  ; first attempt...pretty bad so far
  ; strat: find the occurrence number for each element in 's' and filter out the numbers who's occurrence number is not 1
  ; (define (occurence s v) ; returns the number of occurrences of a list
  ;   (cond
  ;     ((null? s) 0)
  ;     ((= (car s) v)
  ;       (+ 1 (occurence (cdr s) v)))
  ;     (else (occurence (cdr s) v))
  ;   )
  ; )

  ; (define (occurences s) ; get occurrence numbers for a given list, given in descending order
  ;   (if
  ;     (null? s)
  ;     nil
  ;     (cons
  ;       (occurence s (car s))
  ;       (occurences (cdr s))
  ;     )
  ;   )
  ; )

  ; (define (zip a b) ; used for effectively making a 1-to-1 mapping with pairs in the zipped list
  ;   (cond
  ;     ((or (null? a) (null? b)) nil)
  ;     (else (cons (cons (car a) (car b)) (zip (cdr a) (cdr b))))
  ;   )
  ; )

  ; (define arr (zip s (occurences s))) ; zip the OG list and its occurrence numbers
  ; (define raw (filter (lambda (e) (= (cdr e) 1)) arr)) ; filter the ones that occur more than once
  ; (map (lambda (e) (car e)) raw) ; we still got pairs, get the actual numbers instead!

  ; second attempt...looks convoluted but the idea is "simple"
  ; strat:
  ;   - place the first element of the list 's' and ignore the other occurrences of that element
  ;     repeat for all unique elements encountered until we reach the end of the list
  (if (null? s) s (cons (car s) (no-repeats (filter (lambda (e) (not (= (car s) e))) (cdr s)))))
)

; Q10
(define (substitute s old new)
  ; strat:
  ; - kinda copying the structure of the filter method, for each element in 's', if there's a match with
  ;   the 'old' word, put the new one when performing the cons procedure, otherwise, put the original first element;
  ;   iterate through the rest of the list with the same procedure until we reach the end
  ; - if the first element is a pair, run the substitute procedure on that and then process the rest of 's' as usual
  (cond
    ((null? s) nil)
    ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new))) ; process the pair and then keep on going
    ((eq? (car s) old) (cons new (substitute (cdr s) old new))) ; match found, replace and keep on going
    (else (cons (car s) (substitute (cdr s) old new))) ; match not found, skip it and keep on going
  )
)

; Q11
(define (sub-all s olds news)
  (if (or (null? olds) (null? news))
    s ; we are done with subbing if olds or news are empty
    (sub-all ; perform a sub with the first elements of olds and news and check the other sub words
      (substitute s (car olds) (car news))
      (cdr olds) (cdr news)))
)