class C:
    def __del__(self):
        """Called when garbage collected"""
        print(f"im getting collected {self=}")
