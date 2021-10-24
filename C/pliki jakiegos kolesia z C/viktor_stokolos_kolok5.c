#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

struct node {
    int value;
    struct node *left, *right;
};

struct node *new_node(int value) {
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return(node);
}

bool is_leaf(struct node *node){
   if (node == NULL){
      return false;
   } else if ((node->left == NULL) && (node->right == NULL)){
      return true;
   } else {
      return false;
   }
}

int count_left_leaves(struct node *root){
    int amount = 0;

    if (root != NULL){
        if (is_leaf(root->left)){
            amount += 1;
        } else {
            amount += count_left_leaves(root->left);
        }
        amount += count_left_leaves(root->right);
    }

    return amount;
}

struct node *lca(struct node *root, struct node *node1, struct node *node2){
    if (root == NULL){
        return NULL;
    }

    if ((root->value == node1->value) || (root->value == node2->value)){
        return root;
    }
    
    struct node *left_lca = lca(root->left, node1, node2);
    struct node *right_lca = lca(root->right, node1, node2);
    
    if (left_lca && right_lca){
        return root;
    }

    if (left_lca != NULL){
        return left_lca;
    }

    return right_lca;
}

int main() {
    struct node *root = new_node(1);
    root->left = new_node(2);
    root->right = new_node(3);
    root->left->left = new_node(4);
    root->left->right = new_node(5);
    root->right->left = new_node(6);
    root->right->right = new_node(7);
    root->left->left->left = new_node(8);
    root->left->left->right = new_node(9);
    root->left->right->left = new_node(10);
    
    printf("Left leaves amount: %d \n", count_left_leaves(root));
    printf("\n");

    struct node *node1 = new_node(10);
    struct node *node2 = new_node(8);

    struct node *node3 = new_node(3);
    struct node *node4 = new_node(1);

    struct node *node5 = new_node(8);
    struct node *node6 = new_node(7);

    struct node *tmp1 = lca(root, node1, node2); 
    printf("lowest common parent for %d i %d = %d \n", node1->value, node2->value, tmp1->value);

    struct node *tmp2 = lca(root, node3, node4); 
    printf("lowest common parent for %d i %d = %d \n", node3->value, node4->value, tmp2->value);

    struct node *tmp3 = lca(root, node5, node6); 
    printf("lowest common parent for %d i %d = %d \n", node5->value, node6->value, tmp3->value);

    return 0;
}
