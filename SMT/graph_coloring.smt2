(declare-fun color (Int) Int) ;;takes the node and assigns the color

;;edges = [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
;;n_colors = 3

(assert (and (>= (select color 0) 0) (> 3 (select color 0))))
(assert (and (>= (select color 1) 0) (> 3 (select color 1))))
(assert (and (>= (select color 2) 0) (> 3 (select color 2))))
(assert (and (>= (select color 3) 0) (> 3 (select color 3))))
(assert (and (>= (select color 4) 0) (> 3 (select color 4))))

(assert (distinct (select color 0) (select color 2)))
(assert (distinct (select color 0) (select color 4)))
(assert (distinct (select color 1) (select color 2)))
(assert (distinct (select color 1) (select color 3)))
(assert (distinct (select color 1) (select color 4)))
(assert (distinct (select color 3) (select color 2)))
(assert (distinct (select color 3) (select color 4)))

(check-sat)
(get-value ((select color 0) (select color 1) (select color 2) (select color 3) (select color 4)))
