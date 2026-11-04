class Interpreter:

    def __init__(self):
        self.variables = {}
        self.functions = {}

    def evaluate(self, node):

        node_type = node['type']

        # program
        if node_type == 'program':

            for fact in node['facts']:
                self.evaluate(fact)

            if 'exec' in node:
                return self.evaluate(node['exec'])

            return None

        # values
        elif node_type == 'value':
            return node['value']

        # identifiers
        elif node_type == 'id':

            name = node['value']

            if name in self.variables:
                return self.variables[name]

            print(f"Undefined variable: {name}")
            return None

        # assignments
        elif node_type == 'assign':

            value = self.evaluate(node['value'])
            self.variables[node['id']] = value

            return value

        # binary operations
        elif node_type == 'binop':

            left = self.evaluate(node['left'])
            right = self.evaluate(node['right'])
            operator = node['op']

            if operator == '+':
                return left + right

            elif operator == '-':
                return left - right

            elif operator == '*':
                return left * right

            elif operator == '/':

                if right == 0:
                    print("Division by zero")
                    return None

                return left / right

            elif operator == '=':
                return left == right

            elif operator == '<':
                return left < right

            elif operator == '>':
                return left > right

            elif operator == '&':
                return left and right

            elif operator == '|':
                return left or right
            

        # if
        elif node_type == 'if':

            condition = self.evaluate(node['condition'])

            if condition:
                return self.evaluate(node['then'])

            return self.evaluate(node['else'])

        # let
        elif node_type == 'let':

            for fact in node['facts']:
                self.evaluate(fact)

            return self.evaluate(node['body'])

        # function definitions
        elif node_type == 'func_def':

            self.functions[node['name']] = node
            return None

        # exec
        elif node_type == 'exec':
            return self.evaluate(node['stm'])
        
        # function calls
        elif node_type == 'call':

            function_name = node['name']

            if function_name not in self.functions:
                print(f"Undefined function: {function_name}")
                return None

            function_data = self.functions[function_name]

            parameters = function_data['params']
            arguments = node['args']

            local_values = {}

            for i in range(len(parameters)):
                local_values[parameters[i]] = self.evaluate(arguments[i])

            old_memory = self.variables.copy()
            self.variables.update(local_values)

            result = self.evaluate(function_data['body'])

            self.variables = old_memory

            return result