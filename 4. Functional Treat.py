print("\n Welcome to Functional Treat !...")

L1 = [ ]


while True :

    menu = input("""\n Select an option : 
                    1. Input Data
                    2. Display Data Summary (Built-in Functions)
                    3. Calculate Factorial (Recursion)
                    4. Filter Data by Threshold (Lambda Function)
                    5. Sort Data
                    6. Display Dataset Statistics (Return Multiple Values)
                    7. Exit Program     \n
                    Enter your choice : """)



    def  Input_data () :
        global L1

        a = input("\n\n\t\t    Enter data for a 1D array ( Separated by spaces ) : ")
        L1 = list(map(int , a.split()))

        print("\n\n Data has been stored successfully !...")
        print("\n\n" , "*" * 100)



    def  Display_data_summary () :

        print("\n\n The summary of Data is :")

        Total_elements = len(L1)
        Minimum_value = min(L1)
        Maximum_value = max(L1)
        Sum_of_all_value = sum(L1)
        Average_value = sum(L1) / len(L1)

        print("\n Total Elements is :" , Total_elements)
        print(" Minimum value is :" , Minimum_value)
        print(" Maximum value is :" , Maximum_value)
        print(" Sum of all value is :" , Sum_of_all_value)
        print(" The Average of value is :" , Average_value)

        print("\n\n" , "*" * 100)



    def  Calculate_factorial (n) :

        if ( n == 0  or  n == 1 ) :
            return  1

        return  n * Calculate_factorial(n - 1)


    def  Display_factorial () :

        ask = int(input("\n\n\t\t    Enter a number to calculate it's factorial : "))

        print(f"\n\n The Factorial of" , ask , "is :" , Calculate_factorial(ask))
        print("\n\n" , "*" * 100)



    def  Filter_data_by_threshold () :

        Threshold = int(input("\n\n\t\t    Enter a threshold value to filter out data above this value : "))

        A = list(filter(lambda x : x >= Threshold , L1))

        print("\n\n The Filter Data ( values >= " , Threshold , ") :" , A )
        print("\n\n" , "*" * 100)



    def  Sort_data () :

        sort = int(input("""\n\n\t\t    Choose sorting option :  \n
                                1. Ascending
                                2. Descending  \n
                                Enter your choice : """))


        if ( sort == 1 ) :

            Sort = sorted(L1)
            print("\n\n Sorted Data in Ascending order :" , Sort)
            print("\n\n" , "*" * 100)


        elif ( sort == 2 ) :

            Reverse = sorted(L1 , reverse = True)
            print("\n\n Sorted Data in Descending order :" , Reverse)
            print("\n\n" , "*" * 100)


        else :

            print("\n Please enter the valid input !...")



    def  Calculate_dataset_statistics () :

        Minimum_value = min(L1)
        Maximum_value = max(L1)
        Sum_of_all_value = sum(L1)
        Average_value = sum(L1) / len(L1)

        return  Minimum_value , Maximum_value , Sum_of_all_value , Average_value


    def  Display_dataset_statistics () :

        Minimum_value , Maximum_value , Sum_of_all_value , Average_value = Calculate_dataset_statistics()

        print("\n\n Dataset Statics :")
        print("\n Minimum value :" , Minimum_value)
        print(" Maximum value :" , Maximum_value)
        print(" Sum of all values :" , Sum_of_all_value)
        print(" Average_value :" , Average_value)     

        print("\n\n" , "*" * 100)



    if ( menu == '1' ) :
        Input_data()

    elif ( menu == '2' ) :
        Display_data_summary()

    elif ( menu == '3' ) :
        Display_factorial()

    elif ( menu == '4' ) :
        Filter_data_by_threshold()

    elif ( menu == '5' ) :
        Sort_data()

    elif ( menu == '6' ) :
        Display_dataset_statistics()

    elif ( menu == '7' ) :
        exit()

    else :
        print("\n Please enter the valid input !...")