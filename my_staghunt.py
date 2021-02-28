from pythonian import Pythonian
import pyhop    # for operators?
import run_sim

class StagHuntAgent(Pythonian):

    name = "StagHuntAgent"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # TODO: lookup
        for operator in staghunt_htn operators.items(): # TODO: how to get operators?
            self.add_achieve(operator[0], operator[1])


if __name__ == "__main__":
    a = StagHuntAgent(host='localhost', port=9000, localPort=8950, debug=True)
    # AGENT = TestAgent.parse_command_line_args()

# (achieve :receiver TestAgent :content (task :action (test_achieve data)))
# test_acheive is an achieve, but also method defined in same file--does it matter?
