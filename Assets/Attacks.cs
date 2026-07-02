using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Attacks : MonoBehaviour
{

    public bool IsAttacking = false;

    Vector3 mousep;

    public Animator animator;

    public CircleCollider2D swordRange;

    public Camera myCamera;

    bool LeftUp = false;
    bool RightUp = false;

    // Update is called once per frame
    void Update()
    {
        
        mousep = myCamera.ScreenToViewportPoint(Input.mousePosition);

        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            if (IsAttacking == false)
            {
                animator.ResetTrigger("StopAttack");
                if (mousep.x/mousep.y < 1)
                {
                    LeftUp = true;
                }
                if (mousep.x + mousep.y > 1)
                {
                    RightUp = true;
                }
                if (RightUp)
                {
                    if (LeftUp)
                    {
                        animator.SetTrigger("AttackUp");
                    }
                    if (!LeftUp)
                    {
                        animator.SetTrigger("AttackRight");
                    }
                }
                if (!RightUp)
                {
                    if (LeftUp)
                    {
                        animator.SetTrigger("AttackLeft");
                    }
                    if (!LeftUp)
                    {
                        animator.SetTrigger("AttackDown");
                    }
                }
                animator.SetTrigger("Attack");
                IsAttacking = true;
            }
        }
    }

    void AttackEnd()
    {
        IsAttacking = false;
        animator.ResetTrigger("Attack");
        animator.SetTrigger("StopAttack");
        RightUp = false;
        LeftUp = false;
        animator.ResetTrigger("AttackDown");
        animator.ResetTrigger("AttackLeft");
        animator.ResetTrigger("AttackRight");
        animator.ResetTrigger("AttackUp");
    }
}
