class ExecutionOfMiddleware(object):

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print("This Line is from pre-processing of the app") # Appears before preprocessing
        response = self.get_response #Actual view processing
        print("This Line is from post-processing of the app") #After post processing
        return response
