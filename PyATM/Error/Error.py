class Error :
        
    def es(n) :

        """
        To count the error crition -> εs, 
        This method need the variable: n
        which means the signifigant figure.
        """
        error_crition = 0.5 * 10 ** (2 - n)

        return error_crition


    def ea(current_approximation, previous_approximation) :

        """
        To count the approximate estimate percent relative error -> εa.
        This method need the variable: current and previous approximation.
        Then we have to avoid the situation about current approximation is 0,
        if current approximation is zero, then we return -999.
        """

        approximation_error = current_approximation - previous_approximation

        try :
            approximate_relative_error = (approximation_error / current_approximation)
            approximate_percent_relative_error = abs(approximate_relative_error) * 100

            return approximate_percent_relative_error
        except ZeroDivisionError:
            return -999


    def et(true_value, approximation) :   

        """
        To count the true percent relative error -> εt.
        This method need the variable: true value and approximation.
        Then we have to avoid the situation about true value is 0,
        if true value is zero, then we return -999.
        """
        true_error = true_value - approximation

        try :
            true_relative_error = (true_error / true_value)
            true_percent_relative_error = true_relative_error * 100

            return true_percent_relative_error
        except ZeroDivisionError :
            return -999


    def mcepsilon() :

        """
        To get your own computer epsilon.
        """
        epsilon = 1.0

        while (epsilon > 0) :
            xmin = epsilon
            epsilon = epsilon / 2

        return xmin

    def iter_meth(value, error_crition, max_iterator_times) :

        """
        
        """

        iterator_times = 1
        solution = value
        approximate_percent_relative_error = 100

        while True :

            previous_solution = solution
            solution = (solution + (value / solution)) / 2
            iterator_times += 1

            if solution != 0 :
                approximation_error = solution - previous_solution
                approximate_relative_error = (approximation_error / solution)
                approximate_percent_relative_error = abs(approximate_relative_error) * 100

            if (approximate_percent_relative_error < error_crition or 
                iterator_times >= max_iterator_times) :
                break
        
        return solution